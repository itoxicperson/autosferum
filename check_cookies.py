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
driver = webdriver.Chrome(options=options)
chat_code_file = "C:\\sferum\\chat_code.txt"
if os.path.exists(chat_code_file):
    with open(chat_code_file, "r") as file:
        chat_code = file.read().strip()
    url = f"https://web.vk.me/convo/{chat_code}"
else:
    print("Файл с кодом чата не найден.")
driver.get(url)

