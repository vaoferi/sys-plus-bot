# 🚀 START HERE - Telegram Bot Sys+

## 👋 Привіт! Ласкаво просимо до проекту Sys+ Telegram Bot!

Цей бот інтегрує **KeyCRM** з **Telegram** для миттєвих сповіщень про замовлення та клієнтів.

---

## ⚡ ШВИДКИЙ ВИБІР

### 🎯 Хочу швидко запустити (5 хвилин)

➡️ **Відкрийте:** [`QUICKSTART_UA.md`](QUICKSTART_UA.md)

### 📚 Потрібна детальна інструкція

➡️ **Відкрийте:** [`COMPLETE_GUIDE_UA.md`](COMPLETE_GUIDE_UA.md)

### 🔧 Знайомлюся з проектом

➡️ **Відкрийте:** [`FILES_LIST.md`](FILES_LIST.md)

---

## 📁 Структура проекту

```
telegram_bot_keycrm/
│
├── 🟢 ОСНОВНІ ФАЙЛИ
│   ├── app.py                      # Головний код бота
│   ├── keycrm_client.py            # Клієнт KeyCRM API
│   └── requirements.txt            # Python залежності
│
├── ⚙️ КОНФІГУРАЦІЯ
│   ├── .env.example                # Приклад змінних оточення
│   ├── .gitignore                  # Git ignore
│   ├── render.yaml                 # Render конфігурація
│   ├── deploy.bat                  # Windows скрипт запуску
│   └── deploy.ps1                  # PowerShell скрипт
│
├── 📖 ДОКУМЕНТАЦІЯ
│   ├── START_HERE.md               # ЦЕЙ ФАЙЛ - почніть звідси!
│   ├── QUICKSTART_UA.md            # ⚡ Швидкий старт (5 хв)
│   ├── COMPLETE_GUIDE_UA.md        # 📚 Повний гайд
│   ├── README.md                   # Загальна інформація
│   ├── README_RENDER_UA.md         # Детально про Render
│   ├── KEYCRM_WEBHOOK_SETUP_UA.md  # Налаштування KeyCRM
│   ├── EXAMPLES_UA.md              # Приклади роботи
│   └── FILES_LIST.md               # Опис файлів
│
└── 🧪 ТЕСТУВАННЯ
    └── test_local.py               # Локальне тестування
```

---

## 🎯 ПЕРШІ КРОКИ

### Крок 1: Отримати Telegram ID (1 хвилина)

1. Відкрийте Telegram
2. Знайдіть бота **@userinfobot**
3. Натисніть `/start`
4. Скопіюйте свій ID (число)

📝 **Запишіть цей ID!**

---

### Крок 2: Обрати шлях розгортання

#### 🚀 Варіант A: Автоматично (Рекомендується)

**Windows:**
```
Двічі клікніть: deploy.bat
```

**PowerShell:**
```powershell
.\deploy.ps1
```

Скрипт автоматично:
- ✅ Перевірить Git
- ✅ Ініціалізує репозиторій
- ✅ Створить .env файл
- ✅ Встановить залежності
- ✅ Надасть подальші інструкції

---

#### 📝 Варіант B: Вручну

1. Відкрийте [`QUICKSTART_UA.md`](QUICKSTART_UA.md)
2. Виконайте кроки по черзі
3. Бот готовий за 5 хвилин!

---

## 🎓 Навчальні матеріали

### Для початківців

1. **START** → Цей файл (ви тут!)
2. **QUICKSTART** → [`QUICKSTART_UA.md`](QUICKSTART_UA.md)
3. **Приклади** → [`EXAMPLES_UA.md`](EXAMPLES_UA.md)

### Для досвідчених

1. **README** → [`README.md`](README.md)
2. **Render деталі** → [`README_RENDER_UA.md`](README_RENDER_UA.md)
3. **KeyCRM webhook** → [`KEYCRM_WEBHOOK_SETUP_UA.md`](KEYCRM_WEBHOOK_SETUP_UA.md)

### Для всіх

- **Повний гайд** → [`COMPLETE_GUIDE_UA.md`](COMPLETE_GUIDE_UA.md)
- **Опис файлів** → [`FILES_LIST.md`](FILES_LIST.md)

---

## 🔑 Необхідні дані

Вже є в проекті:

✅ **Telegram Bot Token:**
```
8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A
```
Бот: **@Sysplus_bot**

✅ **KeyCRM API Key:**
```
NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA
```

❌ **Потрібно отримати самостійно:**

1. **Telegram Admin ID** - через @userinfobot
2. **GitHub акаунт** - для деплою
3. **Render акаунт** - для хостингу

---

## 🛠️ Технічні деталі

### Технології

- **Python 3.11** - мова програмування
- **Flask 3.0** - веб-сервер
- **Aiogram 3.4** - Telegram Bot API
- **Aiohttp** - асинхронні HTTP запити
- **Render.com** - хостинг

### Архітектура

```
┌─────────────┐      ┌──────────────┐      ┌─────────────┐
│   KeyCRM    │ ───> │  Flask App   │ ───> │  Telegram   │
│   Webhook   │      │  (Render)    │      │     Bot     │
└─────────────┘      └──────────────┘      └─────────────┘
                            │
                            ▼
                     ┌──────────────┐
                     │   Aiogram    │
                     │  Dispatcher  │
                     └──────────────┘
```

### Команди бота

| Команда | Опис |
|---------|------|
| `/start` | Почати роботу |
| `/orders` | Останні замовлення |
| `/clients` | Клієнти |
| `/stats` | Статистика |
| `/help` | Допомога |

---

## 💰 Вартість

**Безкоштовно!**

Render Free тариф включає:
- ✅ 750 годин/місяць (цілодобова робота)
- ✅ 512 MB RAM
- ⚠️ "Засинає" після 15 хв неактивності
- ⚠️ Обмежена продуктивність

**Upgrade:** $7/місяць (Starter tariff)

---

## 🆘 Допомога

### Щось не працює?

1. **Перевірте логи** на Render Dashboard
2. **Прочитайте FAQ** у `COMPLETE_GUIDE_UA.md`
3. **Перевірте змінні** оточення
4. **Протестуйте локально** перед деплоєм

### Де шукати відповіді?

| Проблема | Де шукати |
|----------|-----------|
| Деплой на Render | `README_RENDER_UA.md` |
| KeyCRM не працює | `KEYCRM_WEBHOOK_SETUP_UA.md` |
| Бот мовчить | `COMPLETE_GUIDE_UA.md` (Вирішення проблем) |
| Помилки в коді | `README.md` (Вирішення проблем) |
| Загальні питання | `QUICKSTART_UA.md` |

---

## ✅ Чек-лист успіху

Перевірте перед використанням:

- [ ] Отримали Telegram Admin ID
- [ ] Маєте GitHub акаунт
- [ ] Зареєструвалися на Render
- [ ] Запустили deploy.bat або deploy.ps1
- [ ] Завантажили код на GitHub
- [ ] Створили Web Service на Render
- [ ] Додали всі змінні оточення
- [ ] Health check повертає "ok"
- [ ] Бот відповідає на /start
- [ ] KeyCRM webhook налаштовано

---

## 📞 Контакти

- **Проект:** Sys+
- **Бот:** [@Sysplus_bot](https://t.me/Sysplus_bot)
- **Документація:** Всі файли в цій теці

---

## 🎯 Що далі?

### Після успішного запуску:

1. ✅ Привітайтеся з ботом (`/start`)
2. ✅ Протестуйте команди
3. ✅ Налаштуйте KeyCRM webhook
4. ✅ Створіть тестове замовлення
5. ✅ Перевірте сповіщення

### Розширення функціоналу:

- Додайте більше адміністраторів
- Налаштуйте фільтрацію сповіщень
- Додайте нові команди
- Інтегруйте інші сервіси

---

## 🎁 Бонуси

### Корисні посилання

- [Render Dashboard](https://dashboard.render.com/)
- [GitHub](https://github.com/)
- [Telegram @userinfobot](https://t.me/userinfobot)
- [KeyCRM](https://keycrm.app/)

### Додаткові ресурси

- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Render Docs](https://render.com/docs)
- [KeyCRM API](https://docs.keycrm.app/)
- [Aiogram Docs](https://docs.aiogram.dev/)

---

## 🚀 ГОЛОВНЕ

**Не знаєте з чого почати?**

➡️ **Відкрийте:** [`QUICKSTART_UA.md`](QUICKSTART_UA.md) і слідуйте інструкціям!

**Потрібні деталі?**

➡️ **Відкрийте:** [`COMPLETE_GUIDE_UA.md`](COMPLETE_GUIDE_UA.md)

**Є питання?**

➡️ **Перевірте:** [`FILES_LIST.md`](FILES_LIST.md) для опису всіх файлів

---

**🎉 Успіхів у розробці! Все необхідне вже в цій теці!**
