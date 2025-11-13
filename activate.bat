@echo off
REM Простой способ активации виртуального окружения в CMD
call .venv\Scripts\activate.bat
echo Virtual environment activated!
echo.
echo To deactivate, run: deactivate
cmd /k

