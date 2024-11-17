@echo off
setlocal

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
    pip install --upgrade pip
    REM Удаляем строку с установкой tkinter, так как она не устанавливается через pip
) else (
    echo Используем существующую виртуальную среду...
    call venv\Scripts\activate
)

REM Установка необходимых библиотек
pip install json pandas

REM Запуск вашей программы
echo Запуск main.py...
python Algorithms\main.py

pause
endlocal
