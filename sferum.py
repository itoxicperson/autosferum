import json
import time
import random
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import threading
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--disable-infobars')
options.add_argument('--start-maximized')
user_data_dir = "C:\\sferum\\chrome_profile"
options.add_argument(f"--user-data-dir={user_data_dir}")
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
success_file = 'C:/sferum/success_date.txt'
url_serv = 'https://api.opopop.keenetic.name/'
session_file = "C:\\sferum\\session.txt"
if os.path.exists(session_file):
    with open(session_file, "r") as file:
        session = file.read().strip()
    session = session
else:
    print("Файл с кодом  не найден.")
chat_code_file = "C:\\sferum\\chat_code.txt"
if os.path.exists(chat_code_file):
    with open(chat_code_file, "r") as file:
        chat_code = file.read().strip()
    url = f"https://web.vk.me/convo/{chat_code}"
else:
    print("Файл с кодом чата не найден.")
driver.get(url)
def send_message(message, endpoint):
    data = {
        'code': session,
        'message': message
    }
    while True:
        try:
            response = requests.post(f"{url_serv}/{endpoint}", json=data)
            if response.status_code == 200:
                return True
            else:
                response = requests.post(f"{url_serv}/{endpoint}", json=data)
        except Exception as e:
            response = requests.post(f"{url_serv}/{endpoint}", json=data)

        time.sleep(1)
def check_success_date():
    if os.path.exists(success_file):
        with open(success_file, 'r') as file:
            last_success_date = file.read().strip()
            return last_success_date == datetime.now().strftime("%Y-%m-%d")
    return False
def record_success_date():
    with open(success_file, 'w') as file:
        file.write(datetime.now().strftime("%Y-%m-%d"))
greetings = [
    "привет, как день проходит?",
    "доброе утро всем, какие планы на сегодня?",
    "привет, что интересного у кого?",
    "всем привет! кто чем занимается?",
    "день добрый, как настрой?",
    "приветствую, кто уже успел отличиться?",
    "добрый день, кто с новостями?",
    "как дела у всех? кто чем занят?",
    "привет, какие мысли на сегодня?",
    "привет! как настроение на учебу?",
    "доброго дня, кто готов к новым открытиям?",
    "привет всем, как идет день?",
    "здравствуйте, кто на связи?",
    "день добрый, кто что узнал сегодня?",
    "всем привет! как учеба?",
    "привет, что нового у вас?",
    "приветик, какие успехи?",
    "добрый день, кто как?",
    "всем добрый день, чем занимаетесь?",
    "приветствую всех, что интересного?",
    "всем хорошего дня, как дела?",
    "привет, что нового слышно?",
    "доброго дня! кто уже сделал домашку?",
    "всем привет, чем сегодня удивите?",
    "привет! как все проходит?",
    "здравствуйте! есть что-то интересное?",
    "приветик, что хорошего?",
    "день добрый, кто с какими новостями?",
    "приветствую! как успехи?",
    "привет, как у всех дела?",
    "доброго времени суток, кто на связи?",
    "всем хорошего настроения! кто чем занят?",
    "привет, как вам сегодняшний день?",
    "доброе утро, кто чем порадует?",
    "привет всем, что у кого нового?",
    "всем привет, как учебные дела?",
    "привет, кто что узнал интересного?",
    "доброго дня всем, как настроение?",
    "всем отличного дня, кто на что надеется?",
    "привет! как у вас все?",
    "приветствую всех, какие успехи?",
    "всем привет, кто чем удивит сегодня?",
    "доброго дня! как у вас дела?",
    "привет! как у кого день идет?",
    "доброго времени суток, кто что узнал?",
    "всем доброго дня, кто чем занят?"
]
def check_status():
    response = requests.post(f"{url_serv}/status?code={session}")
    time.sleep(59)
status_thread = threading.Thread(target=check_status)
status_thread.start()
while True:
    current_time = datetime.now().time()
    if current_time >= datetime.strptime("06:40", "%H:%M").time() and current_time <= datetime.strptime("21:55", "%H:%M").time():
        try:
            if check_success_date():
                send_message('Сегодня уже было успешное выполнение отправки сообщений в СФЕРУМ.', 'send_message')
            else:
                driver.get(url)
                time.sleep(5)
                for _ in range(10):
                    message_box = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.CSS_SELECTOR, "span.ComposerInput__input"))
                    )
                    greeting = random.choice(greetings)
                    message_box.clear()
                    message_box.send_keys(greeting)
                    send_button = WebDriverWait(driver, 12).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.ConvoComposer__sendButton--submit"))
                    )
                    send_button.click()
                    time.sleep(1)
                send_message('Только чтоб было успешное выполнение отправки сообщений в СФЕРУМ.', 'send_message')
                record_success_date()
        except Exception as e:
            send_message(f"Произошла ошибка: {e}", 'send_message')
            time.sleep(60)
    else:
        pass
    time.sleep(900)
driver.quit()
