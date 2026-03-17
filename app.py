"""
Sys+ Telegram Bot з інтеграцією KeyCRM
Бот для сповіщення про замовлення та управління клієнтами
Використовує python-telegram-bot замість aiogram (без pydantic!)
"""

import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from keycrm_client import KeyCRMClient

# Налаштування логування
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ініціалізація додатків
app = Flask(__name__)

# Отримуємо токен із змінних оточення
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
KEYCRM_API_KEY = os.getenv('KEYCRM_API_KEY')
TELEGRAM_ADMIN_IDS = [int(id.strip()) for id in os.getenv('TELEGRAM_ADMIN_IDS', '').split(',') if id.strip()]

# Створюємо бота
if TELEGRAM_BOT_TOKEN:
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    keycrm = KeyCRMClient(api_key=KEYCRM_API_KEY, base_url=os.getenv('KEYCRM_BASE_URL', 'https://keycrm.app/api/v2')) if KEYCRM_API_KEY else None
    bot = application.bot
else:
    logger.error("TELEGRAM_BOT_TOKEN not set!")
    application = None
    keycrm = None
    bot = None


@app.route('/webhook/telegram', methods=['POST'])
async def telegram_webhook():
    """Обробка вхідних оновлень від Telegram"""
    try:
        if not application:
            logger.error("Telegram webhook: Application not initialized")
            return {'ok': False}, 500
        update = Update.de_json(request.json, application.bot)
        await application.process_update(update)
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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Команда /start"""
    await update.message.reply_text(
        "👋 Вітаю! Я Sys+ Bot.\n\n"
        "Доступні команди:\n"
        "/orders - Останні замовлення\n"
        "/clients - Клієнти\n"
        "/stats - Статистика\n"
        "/help - Допомога"
    )


async def orders_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показати останні замовлення"""
    try:
        if not keycrm:
            await update.message.reply_text("❌ Сервіс KeyCRM недоступний")
            return
            
        orders = await keycrm.get_recent_orders(limit=5)
        
        if not orders:
            await update.message.reply_text("📭 Замовлень не знайдено")
            return
        
        response = "📦 <b>Останні замовлення:</b>\n\n"
        for order in orders:
            response += f"№{order['id']} - {order['total']} грн ({order['status']})\n"
        
        await update.message.reply_text(response, parse_mode='HTML')
    except Exception as e:
        logger.error(f"Error fetching orders: {e}")
        await update.message.reply_text("❌ Помилка отримання замовлень")


async def clients_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показати клієнтів"""
    try:
        if not keycrm:
            await update.message.reply_text("❌ Сервіс KeyCRM недоступний")
            return
            
        clients = await keycrm.get_recent_clients(limit=5)
        
        if not clients:
            await update.message.reply_text("👥 Клієнтів не знайдено")
            return
        
        response = "👤 <b>Останні клієнти:</b>\n\n"
        for client in clients:
            response += f"{client['name']} - {client.get('phone', 'N/A')}\n"
        
        await update.message.reply_text(response, parse_mode='HTML')
    except Exception as e:
        logger.error(f"Error fetching clients: {e}")
        await update.message.reply_text("❌ Помилка отримання клієнтів")


async def stats_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Показати статистику"""
    try:
        if not keycrm:
            await update.message.reply_text("❌ Сервіс KeyCRM недоступний")
            return
            
        stats = await keycrm.get_statistics()
        
        response = f"""
📊 <b>Статистика KeyCRM</b>

📦 Всього замовлень: {stats.get('total_orders', 0)}
💰 Загальна сума: {stats.get('total_revenue', 0)} грн
👤 Клієнтів: {stats.get('total_clients', 0)}
        """
        
        await update.message.reply_text(response, parse_mode='HTML')
    except Exception as e:
        logger.error(f"Error fetching stats: {e}")
        await update.message.reply_text("❌ Помилка отримання статистики")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Допомога"""
    await update.message.reply_text(
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
        "/help - Допомога",
        parse_mode='HTML'
    )


def setup_handlers():
    """Налаштувати обробники команд"""
    if not application:
        return
    
    # Обробники команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("orders", orders_cmd))
    application.add_handler(CommandHandler("clients", clients_cmd))
    application.add_handler(CommandHandler("stats", stats_cmd))
    application.add_handler(CommandHandler("help", help_cmd))


if __name__ == '__main__':
    # Налаштувати обробники
    setup_handlers()
    
    # Запуск Flask сервера
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
