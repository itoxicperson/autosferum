@echo off
:: Установка необходимых библиотек
python.exe -m pip install --upgrade pip
pip install selenium
pip install requests
pip install tk
pip install webdriver-manager
pip install pillow

echo Установка завершена.
pause
