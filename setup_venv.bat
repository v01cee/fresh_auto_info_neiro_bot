@echo off
echo Creating virtual environment...
python -m venv .venv

echo Installing dependencies...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt

echo.
echo Virtual environment setup complete!
echo.
echo To activate the virtual environment in PowerShell, run:
echo   .venv\Scripts\Activate.ps1
echo.
echo Or in CMD, run:
echo   .venv\Scripts\activate.bat
echo.
echo To deactivate, run:
echo   deactivate
echo.

pause

