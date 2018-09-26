import pytest
import time
from selenium import webdriver
from driver_fixture import *

#1) входит в панель администратора http://localhost/litecart/admin
#2) прокликивает последовательно все пункты меню слева, включая вложенные пункты
#3) для каждой страницы проверяет наличие заголовка (то есть элемента с тегом h1)

def login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()

def quit(driver):
    driver.quit()


def test_h1(driver):
    login(driver)
    menu = driver.find_elements_by_xpath("//li[@id='app-']")
    print (str(len(menu)))

    for i in range(len(menu)):
        menu = driver.find_elements_by_xpath("//*[@id='app-']/a/span[2]")
        menu[i].click()
        submenu = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
        print(str(len(submenu)))

        if len(submenu) <1:
            assert len(driver.find_elements_by_tag_name('h1')) > 0

        if len(submenu) >= 1:
            for j in range(len(submenu)):
                submenu = driver.find_elements_by_xpath("//ul[@class='docs']//li//span")
                submenu[j].click()
                assert len(driver.find_elements_by_tag_name('h1')) > 0

    quit(driver)






























