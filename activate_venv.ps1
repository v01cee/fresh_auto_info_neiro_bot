# Скрипт для активации виртуального окружения в PowerShell
# Использование: .\activate_venv.ps1

Write-Host "Activating virtual environment..." -ForegroundColor Green

# Проверяем существование виртуального окружения
if (!(Test-Path ".venv\Scripts\Activate.ps1")) {
    Write-Host "Virtual environment not found! Creating..." -ForegroundColor Yellow
    python -m venv .venv
    Write-Host "Installing dependencies..." -ForegroundColor Yellow
    .venv\Scripts\python.exe -m pip install --upgrade pip
    .venv\Scripts\python.exe -m pip install -r requirements.txt
}

# Активируем окружение
& .venv\Scripts\Activate.ps1

Write-Host "Virtual environment activated!" -ForegroundColor Green
Write-Host "To deactivate, run: deactivate" -ForegroundColor Cyan

