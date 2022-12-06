from Translater import Translater
import pyautogui
import pyperclip


class TranslatedPyautogui(Translater):

    def __init__(self):
        super().__init__()
        self.duration = 0.2
        self.copy_pixel_color = 48

    def translate(self, text):
        # заполнить область ввода текста
        pyautogui.moveTo(955, 322, self.duration)
        pyautogui.leftClick()
        pyperclip.copy(text)
        # print(pyperclip.paste())

        pyautogui.time.sleep(0.1)

        pyautogui.hotkey('ctrl', 'v')

        current_pixel_color = 0

        while current_pixel_color != self.copy_pixel_color:
            current_pixel_color = pyautogui.pixel(1810, 269)[0]

        # скопировать текст
        pyautogui.moveTo(1807, 266, self.duration)
        pyautogui.leftClick()

        # очистить текст
        pyautogui.moveTo(1235, 269, self.duration)
        pyautogui.leftClick()

        return pyperclip.paste()

