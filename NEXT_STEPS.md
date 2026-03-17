# 🎯 ІНСТРУКЦІЯ: Наступні кроки для деплою

## ✅ Виконано автоматично:

- [x] Перевірено Git (встановлено v2.53.0)
- [x] Ініціалізовано Git репозиторій
- [x] Створено .env файл
- [x] Додано всі файли до Git (git add)
- [ ] **Потрібно зробити коміт** ← Ви тут!
- [ ] **Створити GitHub репозиторій**
- [ ] **Розгорнути на Render**

---

## 🔧 Крок 1: Налаштувати Git користувача

### Відкрийте PowerShell та виконайте команди:

```powershell
# Введіть свій email (той самий що й на GitHub)
git config --global user.email "your-email@example.com"

# Введіть своє ім'я
git config --global user.name "Your Name"
```

### Приклад:
```powershell
git config --global user.email "john@gmail.com"
git config --global user.name "John Doe"
```

---

## 📝 Крок 2: Зробити Git commit

Після налаштування Git виконайте:

```powershell
cd C:\Users\vaoferi\.openclaw\workspace\telegram_bot_keycrm
git commit -m "Initial commit: Sys+ Telegram Bot"
```

---

## 🐙 Крок 3: Створити GitHub репозиторій

### Варіант A: Через веб-інтерфейс (Простіше)

1. Зайдіть на [github.com](https://github.com)
2. Натисніть **"New"** або перейдіть на [github.com/new](https://github.com/new)
3. Заповніть:
   - **Repository name**: `sys-plus-bot`
   - **Description**: `Telegram bot for KeyCRM integration`
   - **Public**: ✅ Так
   - **Initialize with README**: ❌ Ні
4. Натисніть **"Create repository"**

### Варіант B: Через командний рядок (Для досвідчених)

```powershell
# Якщо встановлено GitHub CLI
gh repo create sys-plus-bot --public --source=. --remote=origin
```

---

## 🚀 Крок 4: Завантажити код на GitHub

Після створення репозиторію виконайте:

```powershell
# Перейдіть у теку проекту
cd C:\Users\vaoferi\.openclaw\workspace\telegram_bot_keycrm

# Перейменуйте branch на main
git branch -M main

# Додайте remote (замініть YOUR_USERNAME на ваш нік GitHub)
git remote add origin https://github.com/YOUR_USERNAME/sys-plus-bot.git

# Завантажте код
git push -u origin main
```

### Приклад (якщо ваш GitHub нік "john"):
```powershell
git remote add origin https://github.com/john/sys-plus-bot.git
git push -u origin main
```

---

## ☁️ Крок 5: Розгорнути на Render.com

### 5.1. Увійти на Render

1. Зайдіть на [dashboard.render.com](https://dashboard.render.com)
2. Натисніть **"Sign in with GitHub"**
3. Дозвольте доступ

### 5.2. Створити Web Service

1. Натисніть **"New +"** → **"Web Service"**
2. Оберіть репозиторій `sys-plus-bot`
3. Натисніть **"Connect Repository"**

### 5.3. Налаштувати сервіс

Заповніть поля:

```
Name: sys-plus-bot
Region: Frankfurt, Germany
Branch: main
Root Directory: (залиште порожнім)
Runtime: Python 3
Build Command: pip install -r requirements.txt
Start Command: python app.py
Instance Type: Free
```

### 5.4. Додати змінні оточення

Натисніть **"Advanced"** → **"Add Environment Variable"**:

| Key | Value |
|-----|-------|
| `TELEGRAM_BOT_TOKEN` | `8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A` |
| `KEYCRM_API_KEY` | `NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA` |
| `KEYCRM_BASE_URL` | `https://keycrm.app/api/v2` |
| `TELEGRAM_ADMIN_IDS` | `ВАШ_TELEGRAM_ID` |
| `PORT` | `5000` |

**Важливо:** Не додавайте `RENDER_EXTERNAL_URL` - Render сам її створить!

### 5.5. Отримати Telegram ID

Перед останнім кроком отримайте свій Telegram ID:

1. Відкрийте Telegram
2. Знайдіть бота [@userinfobot](https://t.me/userinfobot)
3. Напишіть `/start`
4. Скопіюйте число (наприклад: `123456789`)
5. Вставте це число в `TELEGRAM_ADMIN_IDS`

### 5.6. Запуск

1. Натисніть **"Create Web Service"**
2. Зачекайте 2-5 хвилин
3. Коли статус буде **"Live"** - готово!

---

## ✅ Крок 6: Перевірка роботи

### 6.1. Health check

Відкрийте в браузері:
```
https://sys-plus-bot.onrender.com/health
```

Має повернутися:
```json
{"status": "ok", "service": "sys_plus_bot"}
```

### 6.2. Тест бота

1. Відкрийте Telegram
2. Знайдіть **@Sysplus_bot**
3. Напишіть `/start`

Бот має відповісти!

---

## 🎁 Шпаргалка: Всі команди разом

### 1. Налаштувати Git:
```powershell
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### 2. Commit:
```powershell
cd C:\Users\vaoferi\.openclaw\workspace\telegram_bot_keycrm
git commit -m "Sys+ Bot initial commit"
```

### 3. Push to GitHub:
```powershell
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/sys-plus-bot.git
git push -u origin main
```

### 4. Render:
- dashboard.render.com → New + → Web Service
- Обрати репозиторій
- Додати змінні оточення
- Create Web Service

---

## 📞 Потрібна допомога?

### Повні інструкції:

- **Швидкий старт**: [`QUICKSTART_UA.md`](QUICKSTART_UA.md)
- **Детальний гайд**: [`COMPLETE_GUIDE_UA.md`](COMPLETE_GUIDE_UA.md)
- **Render інструкція**: [`README_RENDER_UA.md`](README_RENDER_UA.md)
- **KeyCRM webhook**: [`KEYCRM_WEBHOOK_SETUP_UA.md`](KEYCRM_WEBHOOK_SETUP_UA.md)

### Файли проекту:

Всі файли в теці:
```
C:\Users\vaoferi\.openclaw\workspace\telegram_bot_keycrm\
```

---

## 🎯 Фінальний чек-лист

- [ ] Налаштовано Git користувача
- [ ] Зроблено commit
- [ ] Створено GitHub репозиторій
- [ ] Завантажено код (git push)
- [ ] Створено Web Service на Render
- [ ] Додано змінні оточення
- [ ] Отримано Telegram Admin ID
- [ ] Health check працює
- [ ] Бот відповідає на /start
- [ ] Все готово! 🎉

---

**🚀 Успіхів! Ви майже біля фінішу!**
