import pytest
import time
from selenium import webdriver
from driver_fixture import *
import random
import string
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login(driver):
    driver.get("https://ru.ivideon.com/")

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



def test_ivideon_login(driver):
    email = email_generate()
    login(driver)
    driver.find_element_by_xpath("//a[@href='/registraciya/']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='SignUpForm[email]']").click()
    driver.find_element_by_xpath("//input[@name='SignUpForm[email]']").send_keys(email[0])
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='SignUpForm[password]']").click()
    driver.find_element_by_xpath("//input[@name='SignUpForm[password]']").send_keys("test")
    driver.find_element_by_xpath("//input[@value='personal']").click()
    driver.find_element_by_xpath("//input[@value='1']").click()
    driver.find_element_by_xpath("//span[text()='Зарегистрироваться']").click()
    time.sleep(10)
    #WebDriverWait(driver, 4).until(
    #    EC.presence_of_element_located((By.XPATH, "//span[@class='iv-ui-header-navigation-item__link']")))

    #assert len(driver.find_elements_by_xpath("//div[@class)='iv-ui-page-title-header']")) > 0




