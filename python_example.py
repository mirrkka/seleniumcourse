import pytest
import os
import time
from selenium import webdriver
from driver_fixture import *


#@pytest.fixture()
#def driver(request):
#    wd = webdriver.Chrome(os.path.abspath(os.path.join(os.path.dirname(__file__), 'drivers\\chromedriver.exe')))
#
#    def resource_teardown():
#        wd.quit()
#    request.addfinalizer(resource_teardown)
#
#    return wd


def login(driver):
    driver.get("http://open-eshop.stqa.ru/")
    driver.find_element_by_xpath("//div[@class='btn-group pull-right btn-header-group']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='email']").send_keys("demo@open-eshop.com")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("demo")
    driver.find_element_by_xpath("//button[@type='submit']").click()
    driver.find_element_by_xpath("//a[@data-toggle='dropdown']").click()
    driver.find_element_by_xpath("//i[@class='glyphicon glyphicon-shopping-cart']").click()

def logout(driver):
    driver.find_element_by_xpath("//a[@data-toggle='dropdown']").click()
    driver.find_element_by_xpath("//i[@class='glyphicon glyphglyphicon glyphicon-off']").click()


def test_login(driver):
    login(driver)
    time.sleep(2)
    assert len(driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody")) != 0
    time.sleep(1)
    logout(driver)