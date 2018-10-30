import pytest
import time
from selenium import webdriver
from driver_fixture import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


def login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()


def test_log(driver):
    login(driver)
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?app=catalog&doc=catalog']").click()
    products = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[./img and ./a]/a")
    pro = len(products)

    for i in range(pro):
        product = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr/td[./img and ./a]/a")
        print(product[i].get_attribute('href'))
        product[i].click()
        time.sleep(1)
        driver.back()

        logs = driver.get_log("browser")
        if (len(logs)) > 0:
            for l in range(len(logs)):
                  print(l)

        if (len(logs)) == 0:
            print('no logs')

    assert (len(logs)) == 0









