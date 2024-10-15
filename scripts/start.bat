@echo off
mode con: cols=60 lines=40

REM Автоматически определяем путь к скрипту
set "SCRIPT_PATH=%~dp0.."

cd /d "%SCRIPT_PATH%"

REM Переходим в виртуальное окружение
call .\venv\Scripts\activate

REM Запускаем основной Python-скрипт
python main.py

pause
