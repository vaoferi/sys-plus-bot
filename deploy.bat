@echo off
chcp 65001 >nul
cls

echo ========================================
echo Sys+ Telegram Bot - Deployment Helper
echo ========================================
echo.

REM Крок 1: Перевірка Git
echo [1/5] Перевірка Git...
git --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Git знайдено
) else (
    echo ✗ Git не встановлено!
    echo Встановіть Git з https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Крок 2: Ініціалізація Git
echo.
echo [2/5] Ініціалізація Git репозиторію...
if exist ".git" (
    echo ✓ Git репозиторій вже існує
) else (
    git init
    echo ✓ Git репозиторій ініціалізовано
)

REM Крок 3: Створення .env
echo.
echo [3/5] Налаштування .env файлу...
if exist ".env" (
    echo ✓ .env файл вже існує
    echo ⚠️  Пам'ятайте: НЕ комітьте .env у Git!
) else (
    copy .env.example .env
    echo ✓ Створено .env файл з .env.example
    echo ⚠️  Відредагуйте .env та вкажіть свій TELEGRAM_ADMIN_ID
)

REM Крок 4: Перевірка Python
echo.
echo [4/5] Перевірка Python...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo ✓ Python знайдено
    echo Встановлення залежностей...
    pip install -r requirements.txt
    echo ✓ Залежності встановлено
) else (
    echo ⚠️  Python не знайдено
    echo Ви можете встановити залежності пізніше
)

REM Крок 5: Інструкції
echo.
echo ========================================
echo ✓ Підготовку завершено!
echo ========================================
echo.
echo Наступні кроки:
echo.
echo 1. Отримайте Telegram Admin ID:
echo    - Відкрийте Telegram
echo    - Знайдіть бота @userinfobot
echo    - Натисніть /start
echo    - Скопіюйте свій ID
echo.
echo 2. Відредагуйте .env файл:
echo    - Вкажіть свій ID у TELEGRAM_ADMIN_IDS
echo.
echo 3. Створіть GitHub репозиторій:
echo    - github.com/new
echo.
echo 4. Завантажте код на GitHub:
echo    git add .
echo    git commit -m "Initial commit"
echo    git push -u origin main
echo.
echo 5. Розгорніть на Render.com:
echo    - dashboard.render.com
echo    - New + ^→ Web Service
echo.
echo Повна інструкція: README_RENDER_UA.md
echo Швидкий старт: QUICKSTART_UA.md
echo.
echo Успіхів!
echo.
pause
