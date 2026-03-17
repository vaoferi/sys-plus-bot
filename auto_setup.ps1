# Автоматичний скрипт для виконання всіх кроків деплою
# Використання: .\setup_and_deploy.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Sys+ Bot - Автоматичне налаштування" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Крок 1: Перевірка Git
Write-Host "[1/7] Перевірка Git..." -ForegroundColor Yellow
try {
    $gitVersion = git --version
    Write-Host "✓ Git знайдено: $gitVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Git не встановлено!" -ForegroundColor Red
    Write-Host "Встановіть Git з https://git-scm.com/download/win" -ForegroundColor Yellow
    exit 1
}

# Крок 2: Налаштування Git користувача
Write-Host ""
Write-Host "[2/7] Налаштування Git користувача..." -ForegroundColor Yellow

$gitEmail = git config --global user.email
$gitName = git config --global user.name

if (-not $gitEmail -or -not $gitName) {
    Write-Host "Git користувач не налаштовано. Введіть дані:" -ForegroundColor Yellow
    
    $email = Read-Host "Введіть ваш email (той самий що й на GitHub)"
    $name = Read-Host "Введіть ваше ім'я"
    
    git config --global user.email $email
    git config --global user.name $name
    
    Write-Host "✓ Git користувач налаштовано" -ForegroundColor Green
} else {
    Write-Host "✓ Git користувач вже налаштовано: $gitName <$gitEmail>" -ForegroundColor Green
}

# Крок 3: Створення .env файлу
Write-Host ""
Write-Host "[3/7] Перевірка .env файлу..." -ForegroundColor Yellow

if (Test-Path ".env") {
    Write-Host "✓ .env файл вже існує" -ForegroundColor Green
} else {
    Copy-Item ".env.example" ".env"
    Write-Host "✓ Створено .env файл" -ForegroundColor Green
}

Write-Host "⚠️  ВАЖЛИВО: Відредагуйте .env та вкажіть свій TELEGRAM_ADMIN_ID" -ForegroundColor Yellow
Write-Host "   Отримайте ID через бота @userinfobot" -ForegroundColor Gray

# Крок 4: Git add
Write-Host ""
Write-Host "[4/7] Додавання файлів до Git..." -ForegroundColor Yellow
git add .
Write-Host "✓ Файли додано до Git" -ForegroundColor Green

# Крок 5: Git commit
Write-Host ""
Write-Host "[5/7] Створення Git commit..." -ForegroundColor Yellow
$commitMessage = "Initial commit: Sys+ Telegram Bot with KeyCRM integration"
git commit -m $commitMessage

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Commit створено: '$commitMessage'" -ForegroundColor Green
} else {
    Write-Host "⚠️  Неможливо створити commit (можливо, немає змін)" -ForegroundColor Yellow
}

# Крок 6: Інструкції для GitHub
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "[6/7] Створення GitHub репозиторію" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Виконайте ці команди в PowerShell:" -ForegroundColor White
Write-Host ""
Write-Host "# 1. Створіть репозиторій на github.com/new" -ForegroundColor Cyan
Write-Host "# Назва: sys-plus-bot" -ForegroundColor Gray
Write-Host ""
Write-Host "# 2. Після створення виконайте:" -ForegroundColor Cyan
Write-Host "git branch -M main" -ForegroundColor Yellow
Write-Host "git remote add origin https://github.com/ВАШ_НІК/sys-plus-bot.git" -ForegroundColor Yellow
Write-Host "git push -u origin main" -ForegroundColor Yellow
Write-Host ""

# Крок 7: Інструкції для Render
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "[7/7] Деплой на Render.com" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Після завантаження коду на GitHub:" -ForegroundColor White
Write-Host ""
Write-Host "1. Зайдіть на dashboard.render.com" -ForegroundColor Cyan
Write-Host "2. New + → Web Service" -ForegroundColor Cyan
Write-Host "3. Підключіть репозиторій sys-plus-bot" -ForegroundColor Cyan
Write-Host "4. Додайте змінні оточення:" -ForegroundColor Cyan
Write-Host ""
Write-Host "TELEGRAM_BOT_TOKEN = 8261578455:AAHP9G7DnwWVhNa-H3FLr5ZmMRfh367Df7A" -ForegroundColor Yellow
Write-Host "KEYCRM_API_KEY = NGZmYzg4YjY2MTE0OGRkNTBmYWM1NmFjZjE5YWI3MDEwMzc4YmNjZA" -ForegroundColor Yellow
Write-Host "KEYCRM_BASE_URL = https://keycrm.app/api/v2" -ForegroundColor Yellow
Write-Host "TELEGRAM_ADMIN_IDS = ВАШ_TELEGRAM_ID" -ForegroundColor Yellow
Write-Host "PORT = 5000" -ForegroundColor Yellow
Write-Host ""
Write-Host "5. Натисніть Create Web Service" -ForegroundColor Cyan
Write-Host ""

# Фінальні інструкції
Write-Host "========================================" -ForegroundColor Green
Write-Host "✓ Підготовку завершено!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Наступні кроки:" -ForegroundColor White
Write-Host ""
Write-Host "1. Отримайте Telegram Admin ID:" -ForegroundColor Cyan
Write-Host "   - Telegram → @userinfobot → /start" -ForegroundColor Gray
Write-Host ""
Write-Host "2. Відредагуйте .env файл:" -ForegroundColor Cyan
Write-Host "   - Вкажіть свій ID у TELEGRAM_ADMIN_IDS" -ForegroundColor Gray
Write-Host ""
Write-Host "3. Створіть GitHub репозиторій:" -ForegroundColor Cyan
Write-Host "   - github.com/new" -ForegroundColor Gray
Write-Host "   - Назва: sys-plus-bot" -ForegroundColor Gray
Write-Host ""
Write-Host "4. Виконайте команди для push:" -ForegroundColor Cyan
Write-Host "   git branch -M main" -ForegroundColor Yellow
Write-Host "   git remote add origin https://github.com/ВАШ_НІК/sys-plus-bot.git" -ForegroundColor Yellow
Write-Host "   git push -u origin main" -ForegroundColor Yellow
Write-Host ""
Write-Host "5. Розгорніть на Render:" -ForegroundColor Cyan
Write-Host "   - dashboard.render.com" -ForegroundColor Gray
Write-Host "   - New + → Web Service" -ForegroundColor Gray
Write-Host ""
Write-Host "📚 Повна інструкція: NEXT_STEPS.md" -ForegroundColor Cyan
Write-Host "🚀 Швидкий старт: QUICKSTART_UA.md" -ForegroundColor Cyan
Write-Host ""
Write-Host "Успіхів! 🎉" -ForegroundColor Green
Write-Host ""
