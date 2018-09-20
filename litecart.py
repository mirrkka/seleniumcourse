import pytest
import time
from selenium import webdriver
from driver_fixture import *

def login(driver):
    driver.get("http://localhost/litecart/admin/")


def test_login(driver):
    login(driver)
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()
    driver.quit()