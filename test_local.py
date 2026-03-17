"""
Скрипт для локального тестування з ngrok
Дозволяє тестувати вебхуки локально
"""

import os
import subprocess
import time
from dotenv import load_dotenv

# Завантажити змінні оточення
load_dotenv()


def start_ngrok():
    """Запустити ngrok тунель"""
    print("🚀 Запуск ngrok...")
    
    # Перевірити чи встановлений ngrok
    try:
        subprocess.run(['ngrok', '--version'], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Ngrok не знайдено!")
        print("Встановіть ngrok:")
        print("  1. Завантажте з https://ngrok.com/download")
        print("  2. Розпакуйте та додайте в PATH")
        print("  3. Або використайте: pip install pyngrok")
        return None
    
    # Запустити ngrok на порту 5000
    ngrok_process = subprocess.Popen(
        ['ngrok', 'http', '5000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    # Зачекати поки ngrok запуститься
    time.sleep(3)
    
    # Отримати публічний URL
    import requests
    try:
        response = requests.get('http://localhost:4040/api/tunnels')
        data = response.json()
        public_url = data['tunnels'][0]['public_url']
        print(f"✅ Ngrok запущено: {public_url}")
        return public_url
    except Exception as e:
        print(f"❌ Помилка отримання URL: {e}")
        return None


def setup_telegram_webhook(ngrok_url: str):
    """Налаштувати Telegram webhook на ngrok URL"""
    import requests
    
    bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    webhook_url = f"{ngrok_url}/webhook/telegram"
    
    # Видалити старий webhook
    requests.get(f'https://api.telegram.org/bot{bot_token}/deleteWebhook')
    
    # Встановити новий webhook
    response = requests.get(
        f'https://api.telegram.org/bot{bot_token}/setWebhook',
        params={'url': webhook_url}
    )
    
    if response.json().get('ok'):
        print(f"✅ Telegram webhook встановлено: {webhook_url}")
    else:
        print(f"❌ Помилка налаштування Telegram webhook: {response.json()}")


def main():
    """Головна функція"""
    print("=" * 60)
    print("🤖 Sys+ Bot - Локальне тестування з ngrok")
    print("=" * 60)
    
    # Запустити ngrok
    ngrok_url = start_ngrok()
    
    if not ngrok_url:
        print("\n❌ Не вдалося запустити ngrok")
        print("\nАльтернативи:")
        print("  1. Встановіть ngrok: https://ngrok.com/download")
        print("  2. Використайте Render.com для деплою")
        print("  3. Запустіть без ngrok лише для тестування коду")
        return
    
    # Налаштувати Telegram webhook
    setup_telegram_webhook(ngrok_url)
    
    print("\n" + "=" * 60)
    print("Інструкції:")
    print("  1. Відкрийте інший термінал")
    print("  2. Запустіть: python app.py")
    print("  3. Напишіть боту @Sysplus_bot")
    print("  4. Для зупинки натисніть Ctrl+C")
    print("=" * 60)
    
    # Тримати ngrok відкритим
    try:
        ngrok_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Зупинка ngrok...")
        ngrok_process.terminate()


if __name__ == '__main__':
    main()
