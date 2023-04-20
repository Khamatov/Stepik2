from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://anflat.ru/")

# говорим Selenium проверять в течение 2 секунд, пока баннер с куками не станет кликабельным
buttonCloseCoockie = WebDriverWait(browser, 2).until(
        EC.element_to_be_selected((By.CSS_SELECTOR, ".accept-cookie-block-action button"))
    )
buttonCloseCoockie.click()
buttonCloseTimepadBanner = WebDriverWait(browser, 5).until(EC.element_to_be_selected((By.CSS_SELECTOR, ".modal-content-close-btn-img")))
buttonCloseTimepadBanner.click()
buttonLtxwidgetClose = WebDriverWait(browser, 10).until(
        EC.element_to_be_selected((By.CSS_SELECTOR, ".lt-xwidget .lt-xwidget-close i"))
    )
buttonLtxwidgetClose.click()
mainText = browser.find_element(By.CSS_SELECTOR, "data")

# assert "successful" in message.text