from Translater import Translater
import pyautogui
import pyperclip
from dotenv import dotenv_values
config = dotenv_values(".env")


class TranslatedPyautogui(Translater):

    def __init__(self):
        super().__init__()
        self.duration = float(config.get('YANDEX_DURATION'))
        self.copy_pixel_color = int(config.get('YANDEX_COPY_PIXEL_COLOR'))
        self.text_area_center = [int(config.get('YANDEX_TEXTAREA_CENTER_TOP')), int(config.get('YANDEX_TEXTAREA_CENTER_LEFT'))]
        self.copy_btn = [int(config.get('YANDEX_COPY_TOP')), int(config.get('YANDEX_COPY_LEFT'))]
        self.clear_btn = [int(config.get('YANDEX_CLEAR_TEXT_TOP')), int(config.get('YANDEX_CLEAR_TEXT_LEFT'))]

    def translate(self, text):

        # заполнить область ввода текста
        pyautogui.moveTo(self.text_area_center[0], self.text_area_center[1], self.duration)

        pyautogui.leftClick()
        pyperclip.copy(text)
        # print(pyperclip.paste())

        pyautogui.time.sleep(self.duration)

        pyautogui.hotkey('ctrl', 'v')

        current_pixel_color = 0

        while current_pixel_color != self.copy_pixel_color:
            current_pixel_color = pyautogui.pixel(self.copy_btn[0], self.copy_btn[1])[0]

        # скопировать текст
        pyautogui.moveTo(self.copy_btn[0], self.copy_btn[1], self.duration)
        pyautogui.leftClick()

        # очистить текст
        pyautogui.moveTo(self.clear_btn[0], self.clear_btn[1], self.duration)
        pyautogui.leftClick()

        return pyperclip.paste()
