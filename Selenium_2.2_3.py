from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    i = browser.find_element(By.CSS_SELECTOR, "#num1")
    i_2 = i.text
    j = browser.find_element(By.CSS_SELECTOR, "#num2")
    j_2 = j.text
    x = int(i_2) + int(j_2)
    select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
    select.select_by_value(str(x))
    y = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    y.click()
    time.sleep(2)

finally:
    time.sleep(1)
    browser.quit()