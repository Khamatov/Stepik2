from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
link = "https://anflat.ru"
browser.get(link)
buttonCloseCoockie = browser.find_element(By.CSS_SELECTOR, ".accept-cookie-block-action button")
buttonCloseTimepadBanner = browser.find_element(By.CSS_SELECTOR, ".modal-content-close-btn-img")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
buttonCloseCoockie.click()
time.sleep(10)

