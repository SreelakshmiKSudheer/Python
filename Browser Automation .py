from selenium import webdriver
# pip install selenium
# install webdrivre for chrome

browser = webdriver.Chrome("chromedriver-2")
browser.get("https://www.seleniumhq.org")
# first initial the your work and then 

elem = browser.find_element_by_link_text('Download')
elem.click()


#goto web page and click inspect
search = browser.find_element_by_id('q')
search.sendkeys('Download')