from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)
    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    button_2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button_2.click()
    time.sleep(3)

finally:
    time.sleep(1)
    browser.quit()