from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option2.click()
    option3 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    option3.click()
    time.sleep(2)
finally:
    time.sleep(1)
    browser.quit()

