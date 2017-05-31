from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome()
driver.get('http://www.demo.guru99.com/V4/')

login=driver.find_element_by_name('uid')
login.send_keys("mngr74164")
login=driver.find_element_by_name('password')
login.send_keys("pujeveg")
login=driver.find_element_by_name('btnLogin')
login.click()

page_title = driver.title
print ('title of the home page is:'),page_title

time.sleep(2)
driver.close()
