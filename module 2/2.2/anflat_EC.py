from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
link = "https://anflat.ru/"
browser = webdriver.Chrome()
browser.maximize_window()

browser.get(link)

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

buttonLtxwidgetClose = WebDriverWait(browser, 220).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".lt-xwidget .lt-xwidget-close i"))
    )
buttonLtxwidgetClose.click()
print("Лайвтеховский баннер нашёлся и закрылся")
time.sleep(10)
mainText = browser.find_element(By.CSS_SELECTOR, "h1 div")

assert "Купить квартиру в Казани - подбор объектов" in mainText.text
time.sleep(10)