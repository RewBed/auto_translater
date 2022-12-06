from selenium import webdriver
import time

url = "https://translate.yandex.ru/"

driver = webdriver.Chrome(executable_path="C:\\Users\\rewbe\\PycharmProjects\\auto_translater\\chrome\\chromedriver.exe")

try:
    driver.get(url)

    time.sleep(1)
    fake_area = driver.find_element(value='fakeArea')
    fake_area.send_keys("Hello world")

    time.sleep(3)

    #translation_box = driver.find_element("By.CLASS_NAME", "translation-chunk")

    translation_box = driver.find_element(value="translation")
    text = translation_box.text

    print(text)

    clear_btn = driver.find_element(value="clearButton")
    clear_btn.click()

    time.sleep(5)

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()