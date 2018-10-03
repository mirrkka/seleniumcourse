import pytest
import time
from selenium import webdriver
from driver_fixture import *
from selenium.webdriver.support.ui import Select


def login(driver):
    driver.get("http://litecart.stqa.ru/en/")

def test_new_costumer(driver):
    login(driver)
    driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/create_account']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='firstname']").click()
    driver.find_element_by_xpath("//input[@name='firstname']").send_keys("Sasha")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='lastname']").click()
    driver.find_element_by_xpath("//input[@name='lastname']").send_keys("Test")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='address1']").click()
    driver.find_element_by_xpath("//input[@name='address1']").send_keys("TestAddress")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='postcode']").click()
    driver.find_element_by_xpath("//input[@name='postcode']").send_keys("12345")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='city']").click()
    driver.find_element_by_xpath("//input[@name='city']").send_keys("Seattle")
    time.sleep(1)
    driver.find_element_by_xpath("//span[@class='select2-selection__rendered']").click()
    driver.find_element_by_xpath("//input[@type='search']").send_keys("united states")
    select = Select(driver.find_element_by_name("country_code"))
    select.select_by_visible_text("United States")
    driver.find_element_by_name("zone_code").click()
    select_state = Select(driver.find_element_by_name("zone_code"))
    select_state.select_by_visible_text("California")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='phone']").click()
    driver.find_element_by_xpath("//input[@name='phone']").send_keys("+18452245869")





