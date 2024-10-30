import os
import time
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
user_data_dir = "C:\\sferum\\chrome_profile"
chat_code_file = "C:\\sferum\\chat_code.txt"
os.makedirs(user_data_dir, exist_ok=True)
driver = None
def open_browser():
    global driver
    options = Options()
    options.add_argument("--disable-infobars")
    options.add_argument("--start-maximized")
    options.add_argument(f"--user-data-dir={user_data_dir}")
    driver = webdriver.Chrome(options=options)
    driver.get("https://web.vk.me/")
    show_instructions()
def show_instructions():
    root = tk.Tk()
    root.title("Инструкция")
    message = (
        "Пожалуйста, выполните следующие действия:\n"
        "1. Зайдите в свой Сферум.\n"
        "2. Затем зайдите в свой чат класса.\n"
        "После этого код чата будет автоматически извлечён."
    )
    tk.Label(root, text=message).pack(pady=20)
    tk.Button(root, text="Закрыть", command=root.quit).pack(pady=10)
    root.mainloop()
    check_url()
def check_url():
    while True:
        time.sleep(2)
        current_url = driver.current_url
        if current_url.startswith("https://web.vk.me/convo/"):
            chat_code = current_url.split('/')[-1]
            os.makedirs(os.path.dirname(chat_code_file), exist_ok=True)
            with open(chat_code_file, "w") as file:
                file.write(chat_code)
            driver.quit()
            break
open_browser()
