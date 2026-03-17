# 🤖 Sys+ Telegram Bot

Telegram-бот для інтеграції з KeyCRM та сповіщення про замовлення.

## 📋 Можливості

- ✅ Сповіщення про нові замовлення з KeyCRM
- ✅ Сповіщення про зміну статусів замовлень
- ✅ Сповіщення про нових клієнтів
- ✅ Перегляд останніх замовлень (/orders)
- ✅ Перегляд клієнтів (/clients)
- ✅ Статистика продажів (/stats)
- ✅ Webhook інтеграція з KeyCRM

## 🚀 Швидкий старт

### 1. Клонувати репозиторій

```bash
git clone https://github.com/YOUR_USERNAME/sys-plus-bot.git
cd sys-plus-bot
```

### 2. Встановити залежності

```bash
pip install -r requirements.txt
```

### 3. Налаштувати змінні оточення

Створіть файл `.env` на основі `.env.example`:

```bash
cp .env.example .env
```

Відредагуйте `.env` та заповніть своїми даними:

```env
TELEGRAM_BOT_TOKEN=8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A
KEYCRM_API_KEY=NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA
KEYCRM_BASE_URL=https://keycrm.app/api/v2
TELEGRAM_ADMIN_IDS=ВАШ_TELEGRAM_ID
RENDER_EXTERNAL_URL=http://localhost:5000
PORT=5000
```

**Важливо:** Отримайте свій Telegram ID через бота [@userinfobot](https://t.me/userinfobot)

### 4. Запустити локально

```bash
python app.py
```

Бот запуститься на `http://localhost:5000`

### 5. Протестувати

Відкрийте Telegram і знайдіть бота **@Sysplus_bot**, надішліть `/start`

---

## 📱 Команди бота

| Команда | Опис |
|---------|------|
| `/start` | Привітання та початок роботи |
| `/orders` | Показати останні замовлення (5 шт) |
| `/clients` | Показати останніх клієнтів (5 шт) |
| `/stats` | Показати статистику продажів |
| `/help` | Показати довідку по командах |

---

## 🔧 Архітектура

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   KeyCRM    │ ──────> │  Flask App   │ ──────> │  Telegram   │
│   Webhook   │         │  (Render)    │         │     Bot     │
└─────────────┘         └──────────────┘         └─────────────┘
                              │
                              ▼
                       ┌──────────────┐
                       │   Aiogram    │
                       │   Dispatcher │
                       └──────────────┘
```

### Компоненти:

- **Flask** — веб-сервер для обробки webhook'ів
- **Aiogram** — асинхронна бібліотека для Telegram Bot API
- **KeyCRMClient** — клієнт для взаємодії з KeyCRM API
- **Render.com** — хостинг для безсерверного запуску

---

## 📁 Структура проекту

```
telegram_bot_keycrm/
├── app.py                      # Головний додаток Flask + bot handlers
├── keycrm_client.py            # Клієнт для KeyCRM API
├── requirements.txt            # Python залежності
├── render.yaml                 # Конфігурація для Render
├── .env.example                # Приклад змінних оточення
├── .gitignore                  # Git ignore правила
├── README.md                   # Цей файл
└── README_RENDER_UA.md         # Детальна інструкція з деплою
```

---

## 🌐 Deploy на Render.com

Детальна інструкція українською: **[README_RENDER_UA.md](README_RENDER_UA.md)**

### Коротко:

1. Завантажте код на GitHub
2. Створіть Web Service на [Render.com](https://render.com)
3. Підключіть GitHub репозиторій
4. Додайте змінні оточення
5. Отримайте URL сервісу
6. Налаштуйте webhook в KeyCRM

---

## 🔍 Як це працює

### Вхідні події (Telegram → Бот):

1. Користувач надсилає команду боту
2. Telegram відправляє update на `/webhook/telegram`
3. Flask передає update в Aiogram Dispatcher
4. Відповідний handler обробляє команду
5. Бот надсилає відповідь користувачеві

### Вхідні події (KeyCRM → Бот):

1. Створюється замовлення/клієнт в KeyCRM
2. KeyCRM відправляє webhook на `/webhook/keycrm`
3. Flask обробляє подію та формує повідомлення
4. Бот надсилає сповіщення всім адмінам

---

## 🛠️ Локальна розробка

### Встановлення залежностей

```bash
pip install -r requirements.txt
```

### Запуск з отладкою

```bash
# Windows
set FLASK_ENV=development
set FLASK_DEBUG=1
python app.py

# Linux/Mac
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

### Тестування webhook'ів

#### Telegram webhook:

```bash
curl -X POST http://localhost:5000/webhook/telegram \
  -H "Content-Type: application/json" \
  -d '{"update_id": 12345, "message": {"text": "/start", "chat": {"id": 123456}}}'
```

#### KeyCRM webhook:

```bash
curl -X POST http://localhost:5000/webhook/keycrm \
  -H "Content-Type: application/json" \
  -d '{"event": "order.created", "payload": {"id": 1, "total": 1000, "status": "new"}}'
```

---

## 🔐 Безпека

### Зберігання токенів

- ❌ **НЕ** зберігайте `.env` у Git
- ✅ Використовуйте змінні оточення на Render
- ✅ Додайте `.env` у `.gitignore`

### Обмеження доступу

Тільки адміністратори з `TELEGRAM_ADMIN_IDS` отримують сповіщення.

---

## 📊 Моніторинг

### Логи на Render

Dashboard → Ваш сервіс → Logs

### Перевірка статусу

```bash
curl https://your-app.onrender.com/health
```

Відповідь:
```json
{"status": "ok", "service": "sys_plus_bot"}
```

---

## 🐛 Вирішення проблем

### Бот не відповідає

1. Перевірте логи на Render
2. Переконайтеся, що webhook правильно налаштовано
3. Перевірте змінні оточення

### Помилки KeyCRM

1. Перевірте API ключ
2. Переконайтеся, що KeyCRM доступний
3. Перевірте права доступу API

### Вебхуки не працюють

1. Переконайтеся, що URL доступний ззовні
2. Перевірте firewall налаштування
3. Використовуйте [ngrok](https://ngrok.com/) для локального тестування

---

## 🔄 CI/CD

Render автоматично деплоїть при кожному push в GitHub:

```bash
git add .
git commit -m "Fix: bug description"
git push origin main
```

Через 1-2 хвилини оновлення буде на продакшені.

---

## 📚 Документація

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Aiogram Documentation](https://docs.aiogram.dev/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Render Documentation](https://render.com/docs)
- [KeyCRM API Documentation](https://docs.keycrm.app/)

---

## 🤝 Внесок у проект

1. Fork репозиторій
2. Створіть feature branch (`git checkout -b feature/amazing-feature`)
3. Commit зміни (`git commit -m 'Add amazing feature'`)
4. Push до branch (`git push origin feature/amazing-feature`)
5. Відкрийте Pull Request

---

## 📄 Ліцензія

Цей проект створено для внутрішнього використання Sys+.

---

## 👨‍💻 Розробник

Sys+ Team

---

## 🎯 Roadmap

- [ ] Додати підтримку кількох мов (UA/EN)
- [ ] Інтеграція з Google Sheets
- [ ] Розширена аналітика
- [ ] Кнопки та inline меню
- [ ] Розсилка повідомлень
- [ ] Нагадування про замовлення

---

**🚀 Успіхів у розробці!**
