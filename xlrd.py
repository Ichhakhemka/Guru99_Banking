# This script is for taking login test data from excel file


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoAlertPresentException
import time
import xlrd
from xlrd import open_workbook

book = open_workbook('C:\Users\ichha\PycharmProjects\Guru99_Banking\data.xlsx')
sheet=book.sheet_by_index(0)
expected_title ='Guru99 Bank Manager HomePage'
expected_error ='User or Password is not valid'


def setup(self):
    driver = webdriver.Chrome()
    driver.get('http://www.demo.guru99.com/V4/')



for row in range(1, sheet.nrows):
    user_id = sheet.cell(row, 1).value
    password = sheet.cell(row, 2).value
    driver=setup()
    login = driver.find_element_by_name("uid")
    login.send_keys(user_id)
    login = driver.find_element_by_name('password')
    login.send_keys(password)
    login = driver.find_element_by_name('btnLogin')
    login.click()
    time.sleep(2)

    # here we are checking the Pass/Fail Status of the Script.
    # If login credentials are correct,  Alert(Pop up) is NOT present. An Exception is thrown and code in except is executed
    # If login credentials are invalid, Alert is present. Code in try block is executed

    try:
        alert = driver.switch_to_alert()
        alert_text = alert.text
        alert.accept
        if alert_text == expected_error:
            print ' invalid user_id/password test is pass '
        else:
            print ' invalid user_id/password test is fail'

        print alert_text


    except:
        actual_title = driver.title
        if actual_title == expected_title:
            print ' valid user_id/password test is pass '
        else:
            print 'Not Pass'
        print actual_title

    driver.close()