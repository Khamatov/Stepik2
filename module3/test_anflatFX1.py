from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


link = "https://anflat.ru/"
browser = webdriver.Chrome()
browser.maximize_window()
url = browser.current_url
browser.get(link)
#Селекторы:
mainH1 = browser.find_element(By.CSS_SELECTOR, "h1 div")
mainH1Text = mainH1.text
print(mainH1Text)
expectedH1Text = "Купить квартиру в Казани - подбор объектов"
#Функция для проверки
def test_input_text(expected_result, actual_result):
    if actual_result == expected_result:
        return print("Done")
    assert test_input_text(expectedH1Text, mainH1Text) == 'Done'


time.sleep(2)
test_input_text(expectedH1Text, mainH1Text)