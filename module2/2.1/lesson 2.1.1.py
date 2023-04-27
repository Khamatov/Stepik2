from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
inputY = browser.find_element(By.CSS_SELECTOR, ".form-control")
inputY.send_keys(y)
robotCheckBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
robotCheckBox.click()
robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
robotsRule.click()
buttonSubmit = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
buttonSubmit.click()
time.sleep(14)
