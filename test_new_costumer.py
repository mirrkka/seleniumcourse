import pytest
import time
from selenium import webdriver
from driver_fixture import *
from selenium.webdriver.support.ui import Select
import random
import string


def login(driver):
    driver.get("http://litecart.stqa.ru/en/")

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
letters = string.ascii_lowercase[:12]

def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

def email_generate():
    return (generate_random_emails(1, 7))



def test_new_costumer(driver):
    email = email_generate()
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
    time.sleep(1)
    select_state = Select(driver.find_element_by_css_selector("select[name='zone_code']"))
    select_state.select_by_visible_text("Washington")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='phone']").click()
    driver.find_element_by_xpath("//input[@name='phone']").send_keys("+18452245869")
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='email']").click()
    driver.find_element_by_xpath("//input[@name='email']").send_keys(email[0])
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='password']").click()
    driver.find_element_by_xpath("//input[@name='password']").send_keys("test")

    driver.find_element_by_xpath("//input[@name='confirmed_password']").click()
    driver.find_element_by_xpath("//input[@name='confirmed_password']").send_keys("test")
    time.sleep(1)
    driver.find_element_by_xpath("//button[@name='create_account']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/logout']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='email']").click()
    driver.find_element_by_xpath("//input[@name='email']").send_keys(email[0])

    driver.find_element_by_xpath("//input[@name='password']").click()
    driver.find_element_by_xpath("//input[@name='password']").send_keys("test")

    driver.find_element_by_xpath("//button[@name='login']").click()

    driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/logout']").click()














