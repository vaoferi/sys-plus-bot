# 🚀 Інструкція з розгортання на Render.com

## 📋 Передумови

1. Акаунт на [Render.com](https://dashboard.render.com/)
2. GitHub акаунт (для підключення репозиторію)
3. Telegram Bot Token: `8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A`
4. KeyCRM API Key: `NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA`

---

## 🎯 Крок 1: Підготовка репозиторію

### Варіант A: Створити новий GitHub репозиторій
```bash
# У локальній теці проекту
cd C:\Users\vaoferi\.openclaw\workspace\telegram_bot_keycrm

# Ініціалізувати git
git init

# Додати всі файли
git add .

# Зробити commit
git commit -m "Initial commit: Sys+ Telegram Bot"

# Створити репозиторій на GitHub та додати remote
git remote add origin https://github.com/YOUR_USERNAME/sys-plus-bot.git
git push -u origin main
```

### Варіант B: Використати існуючий репозиторій
Просто завантажте файли у свій репозиторій через GitHub UI.

---

## 🎯 Крок 2: Отримати Telegram Admin ID

Щоб бот знав, куди надсилати сповіщення, потрібно дізнатися ваш Telegram ID:

1. Відкрийте Telegram
2. Знайдіть бота **@userinfobot**
3. Натисніть `/start`
4. Бот надішле ваш ID (наприклад: `123456789`)

**Запишіть цей ID!** Він знадобиться при налаштуванні.

---

## 🎯 Крок 3: Розгортання на Render.com

### 3.1. Створити новий Web Service

1. Увійдіть на [dashboard.render.com](https://dashboard.render.com/)
2. Натисніть **"New +"** → **"Web Service"**
3. Оберіть **"Connect a repository"**

### 3.2. Підключити GitHub репозиторій

1. Оберіть свій репозиторій зі списку (`sys-plus-bot`)
2. Натисніть **"Connect Repository"**

### 3.3. Налаштування Web Service

Заповніть поля:

| Поле | Значення |
|------|----------|
| **Name** | `sys-plus-bot` (або будь-яка інша назва) |
| **Region** | `Frankfurt, Germany` (найближче до України) |
| **Branch** | `main` |
| **Root Directory** | залиште порожнім |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python app.py` |
| **Instance Type** | `Free` (безкоштовний тариф) |

### 3.4. Додати змінні оточення (Environment Variables)

Натисніть **"Advanced"** → **"Add Environment Variable"** і додайте:

| Key | Value |
|-----|-------|
| `TELEGRAM_BOT_TOKEN` | `8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A` |
| `KEYCRM_API_KEY` | `NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA` |
| `KEYCRM_BASE_URL` | `https://keycrm.app/api/v2` |
| `TELEGRAM_ADMIN_IDS` | `ВАШ_TELEGRAM_ID` (з Кроку 2) |
| `PORT` | `5000` |

**Важливо:** Після створення сервісу Render автоматично додасть змінну `RENDER_EXTERNAL_URL`. Її не потрібно додавати вручну!

### 3.5. Запуск

1. Натисніть **"Create Web Service"**
2. Зачекайте 2-5 хвилин поки йде деплой
3. Коли статус зміниться на **"Live"** — сервіс готовий!

---

## 🎯 Крок 4: Перевірка роботи

### 4.1. Перевірити health check

Відкрийте в браузері:
```
https://sys-plus-bot.onrender.com/health
```

Має повернутися:
```json
{"status": "ok", "service": "sys_plus_bot"}
```

### 4.2. Протестувати бота

1. Відкрийте Telegram
2. Знайдіть свого бота **@Sysplus_bot**
3. Натисніть `/start`
4. Бот має відповісти привітанням

### 4.3. Протестувати команди

Надішліть боту:
- `/orders` — покаже останні замовлення з KeyCRM
- `/clients` — покаже останніх клієнтів
- `/stats` — покаже статистику
- `/help` — покаже довідку

---

## 🎯 Крок 5: Налаштування вебхуків KeyCRM

Щоб KeyCRM надсилав сповіщення боту:

### 5.1. Отримати URL вебхука

Ваш webhook URL матиме вигляд:
```
https://sys-plus-bot.onrender.com/webhook/keycrm
```

### 5.2. Налаштувати в KeyCRM

1. Увійдіть у свою KeyCRM
2. Перейдіть у **Налаштування** → **Інтеграції** → **Webhooks**
3. Додайте новий webhook:
   - **URL**: `https://sys-plus-bot.onrender.com/webhook/keycrm`
   - **Події**: оберіть потрібні (замовлення, клієнти, статуси)
   - **Метод**: POST
4. Збережіть налаштування

### 5.3. Протестувати вебхук

Створіть тестове замовлення в KeyCRM — бот має надіслати сповіщення вам у Telegram.

---

## 🔧 Вирішення проблем

### ❌ Бот не відповідає на команди

**Причина:** Web Service "заснув" на безкоштовному тарифі

**Рішення:**
1. Відкрийте `https://sys-plus-bot.onrender.com/health`
2. Зачекайте 10-30 секунд
3. Спробуйте знову написати боту

> 💡 На безкоштовному тарифі Render "засинає" після 15 хв неактивності. Перший запит після "сну" обробляється довше.

### ❌ Помилка "Unauthorized" при запиті до KeyCRM

**Причина:** Неправильний API ключ

**Рішення:**
1. Перевірте змінну `KEYCRM_API_KEY` в налаштуваннях Render
2. Переконайтеся, що ключ дійсний в особистому кабінеті KeyCRM

### ❌ Бот не отримує сповіщення від KeyCRM

**Причина:** Неправильно налаштований webhook

**Рішення:**
1. Перевірте URL вебхука в налаштуваннях KeyCRM
2. Переконайтеся, що URL починається з `https://`
3. Перевірте логи в Render Dashboard → Logs

### ❌ Помилки в логах

Перегляньте логи:
1. Render Dashboard → Ваш сервіс → **Logs**
2. Шукайте червоні повідомлення про помилки

---

## 📊 Моніторинг та логи

### Перегляд логів в реальному часі

1. Render Dashboard → Ваш сервіс → **Logs**
2. Або через CLI:
```bash
render logs --service sys-plus-bot
```

### Автоматичний перезапуск

Render автоматично перезапускає сервіс при:
- Збоях в роботі
- Оновленні коду
- Вичерпанні пам'яті

---

## 💰 Тарифи Render

### Free (Безкоштовно)
- ✅ 750 годин на місяць (цілодобова робота)
- ✅ 512 MB RAM
- ⚠️ "Засинає" після 15 хв неактивності
- ⚠️ Обмежена продуктивність

### Starter ($7/місяць)
- ✅ Не "засинає"
- ✅ Більше ресурсів
- ✅ Пріоритетна підтримка

---

## 🔄 Оновлення бота

Після внесення змін у код:

```bash
# Зробити commit змін
git add .
git commit -m "Fix: оновлено обробку замовлень"
git push origin main
```

Render **автоматично** перезапустить сервіс з новими змінами через 1-2 хвилини.

---

## 🎁 Додаткові можливості

### Додати більше адміністраторів

У змінній `TELEGRAM_ADMIN_IDS` вкажіть кілька ID через кому:
```
TELEGRAM_ADMIN_IDS=123456789,987654321,456789123
```

### Змінити порт

Якщо потрібно змінити порт (зазвичай не потрібно):
```
PORT=8080
```

### Додати базу даних

Render дозволяє легко додати PostgreSQL:
1. Dashboard → New → Database
2. Оберіть Free тариф
3. Додайте змінну `DATABASE_URL` у Web Service

---

## 📞 Підтримка

Якщо виникли проблеми:

1. **Перевірте логи** в Render Dashboard
2. **Перевірте змінні оточення** (Environment Variables)
3. **Протестуйте локально** перед деплоєм
4. **Зверніться до документації**:
   - [Render Docs](https://render.com/docs)
   - [Aiogram Docs](https://docs.aiogram.dev/)
   - [KeyCRM API Docs](https://docs.keycrm.app/)

---

## ✅ Чек-лист успішного деплою

- [ ] Створено GitHub репозиторій
- [ ] Завантажено всі файли проекту
- [ ] Створено Web Service на Render
- [ ] Додано всі змінні оточення
- [ ] Отримано Telegram Admin ID
- [ ] Протестовано команду `/start`
- [ ] Протестовано webhook KeyCRM
- [ ] Перевірено логи на відсутність помилок

---

**🎉 Вітаю! Ваш бот успішно розгорнуто на Render.com!**
