# PowerShell скрипт для підготовки проекту до деплою
# Використовується для автоматизації початкових кроків

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Sys+ Telegram Bot - Deployment Helper" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Крок 1: Перевірка чи встановлено Git
Write-Host "[1/5] Перевірка Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✓ Git знайдено: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git не встановлено!" -ForegroundColor Red
    Write-Host "Встановіть Git з https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Крок 2: Ініціалізація Git репозиторію
Write-Host ""
Write-Host "[2/5] Ініціалізація Git репозиторію..." -ForegroundColor Yellow

if (Test-Path ".git") {
    Write-Host "✓ Git репозиторій вже існує" -ForegroundColor Green
} else {
    git init
    Write-Host "✓ Git репозиторій ініціалізовано" -ForegroundColor Green
}

# Крок 3: Створення .env файлу
Write-Host ""
Write-Host "[3/5] Налаштування .env файлу..." -ForegroundColor Yellow

if (Test-Path ".env") {
    Write-Host "✓ .env файл вже існує" -ForegroundColor Green
    Write-Host "⚠️  Пам'ятайте: НЕ комітьте .env у Git!" -ForegroundColor Yellow
} else {
    Copy-Item ".env.example" ".env"
    Write-Host "✓ Створено .env файл з .env.example" -ForegroundColor Green
    Write-Host "⚠️  Відредагуйте .env та вкажіть свій TELEGRAM_ADMIN_ID" -ForegroundColor Yellow
}

# Крок 4: Встановлення залежностей (опціонально)
Write-Host ""
Write-Host "[4/5] Перевірка Python залежностей..." -ForegroundColor Yellow

try {
    $pythonVersion = python --version
    Write-Host "✓ Python знайдено: $pythonVersion" -ForegroundColor Green
    
    Write-Host "Встановлення залежностей..." -ForegroundColor Yellow
    pip install -r requirements.txt
    Write-Host "✓ Залежності встановлено" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Python не знайдено або помилка встановлення" -ForegroundColor Yellow
    Write-Host "Ви можете встановити залежності пізніше" -ForegroundColor Gray
}

# Крок 5: Інструкції для наступних кроків
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "✓ Підготовку завершено!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Наступні кроки:" -ForegroundColor Cyan
Write-Host ""
Write-Host "1. Отримайте Telegram Admin ID:" -ForegroundColor White
Write-Host "   - Відкрийте Telegram" -ForegroundColor Gray
Write-Host "   - Знайдіть бота @userinfobot" -ForegroundColor Gray
Write-Host "   - Натисніть /start" -ForegroundColor Gray
Write-Host "   - Скопіюйте свій ID" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Відредагуйте .env файл:" -ForegroundColor White
Write-Host "   - Відкрийте файл .env" -ForegroundColor Gray
Write-Host "   - Вкажіть свій ID у TELEGRAM_ADMIN_IDS" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Створіть GitHub репозиторій:" -ForegroundColor White
Write-Host "   - Зайдіть на https://github.com" -ForegroundColor Gray
Write-Host "   - Створіть новий публічний репозиторій" -ForegroundColor Gray
Write-Host "   - Назвіть його, наприклад: sys-plus-bot" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Завантажте код на GitHub:" -ForegroundColor White
Write-Host "   git add ." -ForegroundColor Cyan
Write-Host "   git commit -m `"Initial commit: Sys+ Bot`"" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Cyan
Write-Host "   git remote add origin https://github.com/ВАШ_НІК/sys-plus-bot.git" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host ""
Write-Host "5. Розгорніть на Render.com:" -ForegroundColor White
Write-Host "   - Зайдіть на https://dashboard.render.com" -ForegroundColor Gray
Write-Host "   - New + → Web Service" -ForegroundColor Gray
Write-Host "   - Підключіть свій GitHub репозиторій" -ForegroundColor Gray
Write-Host "   - Додайте змінні оточення з .env файлу" -ForegroundColor Gray
Write-Host ""
Write-Host "📚 Повна інструкція: README_RENDER_UA.md" -ForegroundColor Cyan
Write-Host "⚡ Швидкий старт: QUICKSTART_UA.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "Успіхів! 🚀" -ForegroundColor Green
Write-Host ""
