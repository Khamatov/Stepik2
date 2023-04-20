from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
link = "https://anflat.ru"
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, ".accept-cookie-block-action button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(10)
