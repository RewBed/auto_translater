from Translater import Translater
from selenium import webdriver
import time
import pyperclip


class TranslatedSelenium(Translater):

    def __init__(self):
        super().__init__()
        self.url = "https://translate.yandex.ru/"
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\rewbe\\PycharmProjects\\auto_translater\\chrome\\chromedriver.exe")

        self.driver.get(self.url)

    def translate(self, text):

        print('translate')

        time.sleep(1)
        fake_area = self.driver.find_element(value='fakeArea')
        fake_area.click()
        fake_area.send_keys(text)

        print('keys')

        time.sleep(20)

        translation_box = self.driver.find_element(value="translation")
        text = translation_box.text

        clear_btn = self.driver.find_element(value="clearButton")
        clear_btn.click()

        print('clear_btn')

        time.sleep(1)

        return text
