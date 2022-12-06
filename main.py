import pyautogui
import pyperclip
import os
from pathlib import Path

duration = 0.2
copyPixelColor = 48

originPath = 'data/origin/'
translatedPath = 'data/translated/'

for root, dirs, files in os.walk(originPath, topdown=False):
    for name in files:

        f = open(os.path.join(root, name), 'r', encoding='utf-8-sig')

        # заполнить область ввода текста
        pyautogui.moveTo(955, 322, duration)
        pyautogui.leftClick()
        pyperclip.copy(f.read())
        # print(pyperclip.paste())

        pyautogui.time.sleep(0.1)

        pyautogui.hotkey('ctrl', 'v')
        f.close()

        current_pixel_color = 0

        while current_pixel_color != copyPixelColor:
            current_pixel_color = pyautogui.pixel(1810, 269)[0]

        # скопировать текст
        pyautogui.moveTo(1807, 266, duration)
        pyautogui.leftClick()

        # очистить текст
        pyautogui.moveTo(1235, 269, duration)
        pyautogui.leftClick()

        new_dir = os.path.join(translatedPath, os.path.dirname(f.name.replace(originPath, '')))

        print(new_dir)
        print(os.path.exists(new_dir))

        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        new_file = os.path.join(new_dir, os.path.basename(name))

        print(new_file)
        print("\n")

        f = open(new_file, 'w', encoding='utf-8-sig')

        f.write(pyperclip.paste())
        f.close()