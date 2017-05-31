from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get('http://live.guru99.com/index.php/')
expected_text = 'THIS IS DEMO SITE FOR'
choice = 'Name'

# check for expected result 1: verify text on home page
homepage_text = driver.find_element_by_class_name('page-title').text
if homepage_text.find(expected_text) == 0:
    print"Home Page text is matching with expected text"

time.sleep(2)

# check for title 'Mobile' on Mobile list page

mobile = driver.find_element_by_link_text('MOBILE')
mobile.click()
mobile_text = driver.find_element_by_css_selector('.page-title.category-title').text
if mobile_text == 'MOBILE':
    print '"Mobile" is shown on mobile list page'

time.sleep(3)

# select 'Name' from SORT BY drop down menu

select_option = driver.find_element_by_css_selector('select[title="Sort By"]')
all_options = select_option.find_elements_by_tag_name('option')
for option in all_options:
    option_text = option.text
    if option_text.find(choice) >= 0:
        option.click()
        break


        #  verify that all the products are sorted by Name

# Here we are getting all the elemens for phone product names
all_phones = driver.find_elements_by_css_selector('h2.product-name')
phone_list = []
for phone in all_phones:
    name = phone.text
    phone_list.append(name)

# here we are testing that all the phone items are sorted by name
if all(x <= y for x, y in zip(phone_list, phone_list[1:])):
    print 'All the products are sorted by name'

time.sleep(3)
driver.close()