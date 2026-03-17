# 📁 Файли проекту Sys+ Telegram Bot

## Основні файли

| Файл | Призначення |
|------|-------------|
| `app.py` | Головний додаток (Flask + Aiogram) |
| `keycrm_client.py` | Клієнт для роботи з KeyCRM API |
| `requirements.txt` | Python залежності |
| `render.yaml` | Конфігурація для Render.com |

## Конфігураційні файли

| Файл | Призначення |
|------|-------------|
| `.env.example` | Приклад змінних оточення |
| `.gitignore` | Git ignore правила |

## Документація

| Файл | Призначення |
|------|-------------|
| `README.md` | Загальна документація проекту |
| `README_RENDER_UA.md` | **ДЕТАЛЬНА** інструкція з деплою на Render |
| `QUICKSTART_UA.md` | **ШВИДКИЙ СТАРТ** - 5 хвилин до запуску |
| `FILES_LIST.md` | Цей файл |

## Тестування

| Файл | Призначення |
|------|-------------|
| `test_local.py` | Скрипт для локального тестування з ngrok |

---

## 🚀 Як почати

### Варіант 1: Швидкий старт (5 хв)

1. Відкрийте **`QUICKSTART_UA.md`**
2. Виконайте кроки по черзі
3. Бот готовий!

### Варіант 2: Детальне вивчення

1. Відкрийте **`README.md`**
2. Вивчіть архітектуру та можливості
3. Налаштуйте локальне оточення
4. Зробіть деплой на Render

### Варіант 3: Повна інструкція з деплою

1. Відкрийте **`README_RENDER_UA.md`**
2. Детально пройдіться по кожному кроці
3. Отримайте глибоке розуміння процесу

---

## 📋 Необхідні дані

Вже є у файлах:

✅ **Telegram Bot Token:**
```
8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A
```
Бот: **@Sysplus_bot**

✅ **KeyCRM API Key:**
```
NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA
```

❌ **Потрібно отримати:**

1. **Telegram Admin ID** - через @userinfobot
2. **GitHub акаунт** - для деплою
3. **Render акаунт** - для хостингу

---

## 🎯 Структура проекту

```
telegram_bot_keycrm/
├── app.py                      # 🟢 ГОЛОВНИЙ ФАЙЛ - Flask + бот
├── keycrm_client.py            # 🔵 Клієнт KeyCRM API
├── requirements.txt            # 📦 Залежності Python
├── render.yaml                 # ⚙️  Конфіг Render
├── .env.example                # 📝 Приклад .env
├── .gitignore                  # 🚫 Git ignore
├── test_local.py               # 🧪 Локальне тестування
├── README.md                   # 📖 Загальна документація
├── README_RENDER_UA.md         # 📚 ДЕТАЛЬНИЙ гайд по Render
├── QUICKSTART_UA.md            # ⚡ ШВИДКИЙ СТАРТ
└── FILES_LIST.md               # 📁 Цей файл
```

---

## 🔑 Змінні оточення

Які потрібно налаштувати на Render:

```bash
TELEGRAM_BOT_TOKEN=8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A
KEYCRM_API_KEY=NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA
KEYCRM_BASE_URL=https://keycrm.app/api/v2
TELEGRAM_ADMIN_IDS=ВАШ_TELEGRAM_ID
PORT=5000
```

**Важливо:** 
- `RENDER_EXTERNAL_URL` додається автоматично!
- `TELEGRAM_ADMIN_IDS` - ваш ID з @userinfobot

---

## 🎓 Навчальний план

### Рівень 1: Новачок
1. Прочитати `QUICKSTART_UA.md`
2. Запустити на Render за 5 хвилин
3. Протестувати базові команди

### Рівень 2: Середній
1. Прочитати `README.md`
2. Вивчити архітектуру
3. Налаштувати локальне оточення
4. Модифікувати код під свої потреби

### Рівень 3: Просунутий
1. Прочитати `README_RENDER_UA.md`
2. Вивчити всі нюанси деплою
3. Налаштувати CI/CD
4. Додати нові функції

---

## 💡 Поради

### ✅ Що робити

- Використовуйте `QUICKSTART_UA.md` для швидкого старту
- Зберігайте токени в змінних оточення
- Регулярно робіть commit змін
- Моніжте логи на Render

### ❌ Чого уникати

- Не комітьте `.env` файл у Git
- Не зберігайте токени в коді
- Не ігноруйте логи помилок
- Не забувайте тестувати локально перед деплоєм

---

## 🔗 Корисні посилання

- [Render Dashboard](https://dashboard.render.com/)
- [Telegram @userinfobot](https://t.me/userinfobot)
- [KeyCRM Docs](https://docs.keycrm.app/)
- [Render Docs](https://render.com/docs)
- [Aiogram Docs](https://docs.aiogram.dev/)

---

## 🆘 Допомога

### Якщо щось не працює:

1. Перевірте логи на Render
2. Переконайтеся, що всі змінні оточення правильні
3. Прочитайте відповідний розділ у `README_RENDER_UA.md`
4. Перевірте, що GitHub репозиторій оновлено

### Де шукати відповіді:

- Помилки деплою → `README_RENDER_UA.md` (розділ "Вирішення проблем")
- Бот не відповідає → `README.md` (розділ "Вирішення проблем")
- KeyCRM не працює → перевірте API ключ
- Вебхуки не приходять → перевірте URL webhook

---

## 🎯 Наступні кроки

Після успішного запуску:

1. ✅ Привітайтеся з ботом (`/start`)
2. ✅ Протестуйте команди (`/orders`, `/clients`, `/stats`)
3. ✅ Налаштуйте KeyCRM webhook
4. ✅ Створіть тестове замовлення
5. ✅ Перевірте сповіщення в Telegram

---

## 📞 Контакти

Проект: **Sys+**
Бот: **@Sysplus_bot**

---

**🚀 Успіхів! Все необхідне вже у цій теці!**
