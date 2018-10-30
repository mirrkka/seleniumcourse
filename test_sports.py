import pytest
import time
from selenium import webdriver
from driver_fixture import *

def login(driver):
    driver.get("https://www.sports.ru/")

def test_sport(driver):
    login(driver)
    links = []
    menu = driver.find_elements_by_xpath("//a[@class='main-menu__link']")
    print(str(len(menu)))

    for link in menu:
        print(link.get_attribute('href'))
        links.append(link.get_attribute('href'))
        print(links)

    for i in links:
        driver.get(i)
        driver.back()
