@echo off
REM Получаем путь к директории, в которой находится данный bat-файл
set "SCRIPT_DIR=%~dp0"
cd "%SCRIPT_DIR%"

REM Проверяем установлен ли Python
where python >nul 2>nul
if errorlevel 1 (
    echo Python не установлен. Пожалуйста, установите Python.
    pause
    exit /b
)

REM Проверяем, существует ли виртуальная среда
if not exist venv (
    echo Создаем виртуальную среду...
    python -m venv venv
    echo Установка необходимых пакетов...
    call venv\Scripts\activate
    pip install tkinter json pandas
) else (
    echo Используем существующую виртуальную среду...
    call venv\Scripts\activate
)

REM Запуск основного скрипта
echo Запуск main.py...
python main.py
pause
