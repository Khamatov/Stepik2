from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, "#num1")
y_element = browser.find_element(By.CSS_SELECTOR, "#num2")
x = int(x_element.text)
y = int(y_element.text)

summ = str(x + y)

browser.find_element(By.TAG_NAME, "select").click()
opt = browser.find_element(By.CSS_SELECTOR, f"option[value='{summ}']")
opt.click()
summitButton = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
summitButton.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


time.sleep(15)
print(summ)
