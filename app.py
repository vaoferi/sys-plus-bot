"""
Sys+ Telegram Bot з інтеграцією KeyCRM
Бот для сповіщення про замовлення та управління клієнтами
"""

import os
import logging
from flask import Flask, request, abort
from aiogram import Bot, Dispatcher, types
from aiogram.utils.web_app import check_webapp_signature
from keycrm_client import KeyCRMClient

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ініціалізація додатків
app = Flask(__name__)
bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))
dp = Dispatcher()
keycrm = KeyCRMClient(api_key=os.getenv('KEYCRM_API_KEY'))

# Глобальна змінна для webhook URL
WEBHOOK_URL = os.getenv('RENDER_EXTERNAL_URL', 'http://localhost:5000')


@app.route('/webhook/telegram', methods=['POST'])
async def telegram_webhook():
    """Обробка вхідних оновлень від Telegram"""
    try:
        update = types.Update(**request.json)
        await dp.feed_update(bot, update)
        return {'ok': True}
    except Exception as e:
        logger.error(f"Error processing update: {e}")
        return {'ok': False}


@app.route('/webhook/keycrm', methods=['POST'])
async def keycrm_webhook():
    """Обробка вебхуків від KeyCRM"""
    try:
        data = request.json
        logger.info(f"Received KeyCRM webhook: {data}")
        
        # Обробка різних типів подій
        event_type = data.get('event', {})
        
        if event_type == 'order.created':
            await handle_new_order(data)
        elif event_type == 'order.status_changed':
            await handle_status_change(data)
        elif event_type == 'client.created':
            await handle_new_client(data)
        
        return {'ok': True}
    except Exception as e:
        logger.error(f"Error processing KeyCRM webhook: {e}")
        return {'ok': False}, 500


@app.route('/health', methods=['GET'])
def health_check():
    """Перевірка здоров'я додатку"""
    return {'status': 'ok', 'service': 'sys_plus_bot'}


async def handle_new_order(data):
    """Обробка нового замовлення"""
    order = data.get('payload', {})
    order_id = order.get('id')
    total = order.get('total', 0)
    
    message = f"""
🛒 <b>Нове замовлення!</b>

📦 Замовлення №{order_id}
💰 Сума: {total} грн
👤 Клієнт: {order.get('client_name', 'Невідомо')}

Переглянути: {os.getenv('KEYCRM_BASE_URL')}/orders/{order_id}
    """
    
    # Надіслати адмінам
    await send_to_admins(message)


async def handle_status_change(data):
    """Зміна статусу замовлення"""
    order = data.get('payload', {})
    order_id = order.get('id')
    new_status = order.get('status', 'Unknown')
    
    message = f"""
📊 <b>Статус замовлення змінено</b>

📦 Замовлення №{order_id}
✅ Новий статус: {new_status}
    """
    
    await send_to_admins(message)


async def handle_new_client(data):
    """Новий клієнт"""
    client = data.get('payload', {})
    client_name = client.get('name', 'Невідомо')
    
    message = f"""
👤 <b>Новий клієнт</b>

Ім'я: {client_name}
Телефон: {client.get('phone', 'Не вказано')}
    """
    
    await send_to_admins(message)


async def send_to_admins(message: str):
    """Надіслати повідомлення всім адмінам"""
    admin_ids = get_admin_ids()
    
    for admin_id in admin_ids:
        try:
            await bot.send_message(
                chat_id=admin_id,
                text=message,
                parse_mode='HTML'
            )
        except Exception as e:
            logger.error(f"Failed to send message to admin {admin_id}: {e}")


def get_admin_ids():
    """Отримати список ID адміністраторів"""
    admin_ids_str = os.getenv('TELEGRAM_ADMIN_IDS', '')
    return [int(id.strip()) for id in admin_ids_str.split(',') if id.strip()]


@dp.message(lambda message: message.text == '/start')
async def cmd_start(message: types.Message):
    """Команда /start"""
    await message.answer(
        "👋 Вітаю! Я Sys+ Bot.\n\n"
        "Доступні команди:\n"
        "/orders - Останні замовлення\n"
        "/clients - Клієнти\n"
        "/stats - Статистика\n"
        "/help - Допомога"
    )


@dp.message(lambda message: message.text == '/orders')
async def cmd_orders(message: types.Message):
    """Показати останні замовлення"""
    try:
        orders = await keycrm.get_recent_orders(limit=5)
        
        if not orders:
            await message.answer("📭 Замовлень не знайдено")
            return
        
        response = "📦 <b>Останні замовлення:</b>\n\n"
        for order in orders:
            response += f"№{order['id']} - {order['total']} грн ({order['status']})\n"
        
        await message.answer(response, parse_mode='HTML')
    except Exception as e:
        logger.error(f"Error fetching orders: {e}")
        await message.answer("❌ Помилка отримання замовлень")


@dp.message(lambda message: message.text == '/clients')
async def cmd_clients(message: types.Message):
    """Показати клієнтів"""
    try:
        clients = await keycrm.get_recent_clients(limit=5)
        
        if not clients:
            await message.answer("👥 Клієнтів не знайдено")
            return
        
        response = "👤 <b>Останні клієнти:</b>\n\n"
        for client in clients:
            response += f"{client['name']} - {client.get('phone', 'N/A')}\n"
        
        await message.answer(response, parse_mode='HTML')
    except Exception as e:
        logger.error(f"Error fetching clients: {e}")
        await message.answer("❌ Помилка отримання клієнтів")


@dp.message(lambda message: message.text == '/stats')
async def cmd_stats(message: types.Message):
    """Показати статистику"""
    try:
        stats = await keycrm.get_statistics()
        
        response = f"""
📊 <b>Статистика KeyCRM</b>

📦 Всього замовлень: {stats.get('total_orders', 0)}
💰 Загальна сума: {stats.get('total_revenue', 0)} грн
👤 Клієнтів: {stats.get('total_clients', 0)}
        """
        
        await message.answer(response, parse_mode='HTML')
    except Exception as e:
        logger.error(f"Error fetching stats: {e}")
        await message.answer("❌ Помилка отримання статистики")


@dp.message(lambda message: message.text == '/help')
async def cmd_help(message: types.Message):
    """Допомога"""
    await message.answer(
        "ℹ️ <b>Допомога</b>\n\n"
        "Цей бот інтегрований з KeyCRM і дозволяє:\n"
        "- Отримувати сповіщення про нові замовлення\n"
        "- Переглядати інформацію про клієнтів\n"
        "- Отримувати статистику продажів\n\n"
        "Команди:\n"
        "/start - Почати роботу\n"
        "/orders - Останні замовлення\n"
        "/clients - Клієнти\n"
        "/stats - Статистика\n"
        "/help - Допомога"
    )


def setup_webhook():
    """Налаштувати webhook для Telegram"""
    webhook_url = f"{WEBHOOK_URL}/webhook/telegram"
    
    try:
        bot.set_webhook(webhook_url)
        logger.info(f"Telegram webhook встановлено: {webhook_url}")
    except Exception as e:
        logger.error(f"Error setting Telegram webhook: {e}")


if __name__ == '__main__':
    # Налаштування webhook при запуску
    setup_webhook()
    
    # Запуск Flask сервера
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
