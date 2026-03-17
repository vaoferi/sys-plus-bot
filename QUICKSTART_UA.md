# 🚀 ШВИДКИЙ СТАРТ - Telegram Bot для Render.com

## ⚡ 5 хвилин до запуску

### Крок 1: GitHub (2 хв)

1. Створіть новий репозиторій на GitHub
2. Завантажте туди всі файли з цієї теки

**Або через командний рядок:**
```bash
cd C:\Users\vaoferi\.openclaw\workspace\telegram_bot_keycrm

git init
git add .
git commit -m "Sys+ Bot initial"

# Створіть репозиторій на github.com, потім:
git remote add origin https://github.com/ВАШ_НІК/sys-plus-bot.git
git push -u origin main
```

---

### Крок 2: Отримати Telegram ID (1 хв)

1. Відкрийте Telegram
2. Знайдіть бота **@userinfobot**
3. Натисніть `/start`
4. Скопіюйте свій ID (наприклад: `123456789`)

---

### Крок 3: Render.com (2 хв)

#### 3.1. Реєстрація

1. Зайдіть на [dashboard.render.com](https://dashboard.render.com/)
2. Увійдіть через GitHub акаунт

#### 3.2. Створення сервісу

1. Натисніть **"New +"** → **"Web Service"**
2. Оберіть свій репозиторій `sys-plus-bot`
3. Заповніть:

| Поле | Значення |
|------|----------|
| Name | `sys-plus-bot` |
| Region | `Frankfurt, Germany` |
| Branch | `main` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python app.py` |
| Instance Type | `Free` |

#### 3.3. Змінні оточення

Натисніть **"Advanced"** → додайте змінні:

```
TELEGRAM_BOT_TOKEN = 8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A
KEYCRM_API_KEY = NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA
KEYCRM_BASE_URL = https://keycrm.app/api/v2
TELEGRAM_ADMIN_IDS = ВАШ_ID_З_КРОКУ_2
PORT = 5000
```

**Важливо:** Не додавайте `RENDER_EXTERNAL_URL` вручну - Render сам її створить!

#### 3.4. Запуск

Натисніть **"Create Web Service"** і зачекайте 2-5 хвилин.

---

### Крок 4: Перевірка (1 хв)

#### 4.1. Health check

Відкрийте в браузері:
```
https://sys-plus-bot.onrender.com/health
```

Має бути: `{"status": "ok", "service": "sys_plus_bot"}`

#### 4.2. Тест бота

1. Відкрийте Telegram
2. Знайдіть **@Sysplus_bot**
3. Напишіть `/start`
4. Бот має відповісти!

---

## 🎉 Готово!

Бот працює! Тепер налаштуйте KeyCRM webhook:

### KeyCRM Webhook

1. URL: `https://sys-plus-bot.onrender.com/webhook/keycrm`
2. Події: замовлення, клієнти, статуси
3. Метод: POST

---

## 📱 Доступні команди

- `/start` - Почати роботу
- `/orders` - Останні замовлення
- `/clients` - Клієнти
- `/stats` - Статистика
- `/help` - Допомога

---

## 🔧 Якщо щось не працює

### Бот не відповідає

1. Відкрийте `https://sys-plus-bot.onrender.com/health`
2. Зачекайте 30 секунд (сервіс "прокидається")
3. Спробуйте знову `/start`

### Помилки

1. Render Dashboard → Ваш сервіс → **Logs**
2. Дивіться червоні повідомлення

### Перевірити змінні

Render Dashboard → Ваш сервіс → **Environment**

---

## 💰 Вартість

**Безкоштовно!** 

На Free тарифі:
- 750 годин/місяць (цілодобова робота)
- 512 MB RAM
- ⚠️ "Засинає" після 15 хв неактивності (але швидко "прокидається")

---

## 📞 Питання?

Дивіться повну інструкцію: **README_RENDER_UA.md**

---

**✅ Вітаю! Бот готовий до роботи!**
