from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.commom.by import By
import time

driver = webdriver.Chrome('chromedriver-2')
driver.get('https://web.watsapp.com/')
wait = WebDriverWait(driver,600)

target = '"Ravikiran"'                      # friend
string = "Message sent using Python"        # message to be sent to friend

x_arg = '//span[contains(@title, ' + target + ')]'          # span -- collection of elements
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()


input_box = driver.find_element_by_class_name('_1Plpp')

for i in range(50):
    input_box.send_keys(string+Keys.ENTER)
    
