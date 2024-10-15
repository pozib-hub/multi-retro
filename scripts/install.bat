@echo off
mode con: cols=60 lines=40

REM Автоматически определяем путь к корню
cd /d "%~dp0.."

REM Создаем виртуальное окружение
echo Creating a virtual environment
echo loading...
python -m venv venv

REM Переходим в виртуальное окружение
call .\venv\Scripts\activate

REM Устанавливаем зависимости
pip install requests selenium python-dotenv

REM Завершаем выполнение
echo success.
exit