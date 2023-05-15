from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

link = "https://anflat:daewoo.7@site-test.anflat.ru/"
browser = webdriver.Chrome()
browser.maximize_window()

browser.get(link)
# Селекторы:
mainH1 = browser.find_element(By.CSS_SELECTOR, "h1 div")
mainH1Text = mainH1.text
expectedH1Text = "Купить квартиру в Казани - подбор объектов"


# говорим Selenium проверять в течение 2 секунд, пока баннер с куками не станет кликабельным
buttonCloseCoockie = WebDriverWait(browser, 2).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".accept-cookie-block-action button"))
)
buttonCloseCoockie.click()
print("Куки нашлись и закрылись")

buttonCloseTimepadBanner = WebDriverWait(browser, 11).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".modal-content-close-btn-img"))
)
buttonCloseTimepadBanner.click()
print("Таймпадовский баннер нашёлся и закрылся")

assert expectedH1Text == mainH1Text, f"Строка {mainH1Text} не равна {expectedH1Text}"
print("Строка h1 найдена")
time.sleep(2)
