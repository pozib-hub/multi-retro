@echo off
mode con: cols=60 lines=40

REM Автоматически определяем путь к корню
cd /d "%~dp0.."

echo "%~dp0..".

git pull

REM Создаем виртуальное окружение
echo Creating a virtual environment
echo loading...
python -m venv venv

REM Переходим в виртуальное окружение
call .\venv\Scripts\activate

REM Устанавливаем зависимости
pip install pygetwindow pyautogui keyboard pyscreeze psutil opencv-python pytesseract apscheduler

REM Завершаем выполнение
echo success.
pause