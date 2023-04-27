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
expectedH1Text = "Купить квартиру в Казани - подбор объектов"
#Функция для проверки
def test_input_text(expected_result, actual_result):
    assert expected_result != actual_result, f"expected {expected_result}, got {actual_result}"


# говорим Selenium проверять в течение 2 секунд, пока баннер с куками не станет кликабельным
buttonCloseCoockie = WebDriverWait(browser, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".accept-cookie-block-action button"))
    )
buttonCloseCoockie.click()
print("Куки нашлись и закрылись")

buttonCloseTimepadBanner = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-content-close-btn-img"))
    )
buttonCloseTimepadBanner.click()
print("Таймпадовский баннер нашёлся и закрылся")

# buttonLtxwidgetClose = WebDriverWait(browser, 220).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, ".lt-xwidget .lt-xwidget-close i"))
#     )
# buttonLtxwidgetClose.click()
# print("Лайвтеховский баннер нашёлся и закрылся")
# time.sleep(10)

assert expectedH1Text == mainH1Text, f"Строка {mainH1Text} не равна {expectedH1Text}"
print("Строка h1 найдена")
time.sleep(2)
test_input_text(expectedH1Text, mainH1Text)
