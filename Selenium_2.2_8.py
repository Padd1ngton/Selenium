from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    option1 = browser.find_element(By.NAME, "firstname")
    option1.send_keys("11")
    option2 = browser.find_element(By.NAME, "lastname")
    option2.send_keys("11")
    option3 = browser.find_element(By.NAME, "email")
    option3.send_keys("11")
    option4 = browser.find_element(By.ID, "file")
    file_path = 'C:\\Users\\pocht\\Pictures\\Cyberpunk 2077\\photomode_08032021_020455.PNG'
    option4.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()
    time.sleep(3)
finally:
    time.sleep(1)
    browser.quit()