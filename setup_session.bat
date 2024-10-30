@echo off
:: Создание папки C:\sferum, если она еще не существует
if not exist "C:\sferum" (
    mkdir "C:\sferum"
)

:: Показать инструкции
echo.
echo Добро пожаловать! Пожалуйста, следуйте инструкции ниже:
echo.
echo "Вам нужно получить session code от администратора."
echo "Для получения session code, свяжитесь с администратором по ссылке:"
echo "https://example.com/admin"  :: Замените ссылку на нужную
echo.

:: Запрос session code у пользователя
set /p session_code="Введите session code, полученный от администратора: "

:: Проверка ввода session code
if "%session_code%"=="" (
    echo Ошибка: Вы не ввели session code. Попробуйте еще раз.
    pause
    exit /b
)

:: Сохранение session code в файл session.txt
echo %session_code% > "C:\sferum\session.txt"
echo Session code сохранен в C:\sferum\session.txt
pause
