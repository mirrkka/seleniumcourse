import pytest
import time
from selenium import webdriver
from driver_fixture import *
import os
from selenium.webdriver.support.ui import Select

def login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()

def quit(driver):
    driver.quit()

def test_add_new_product(driver):
    login(driver)
    driver.find_element_by_xpath("//span[text()='Catalog']").click()
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?category_id=0&app=catalog&doc=edit_product']").click()
    time.sleep(1)
    #general
    driver.find_element_by_xpath("//input[@name='name[en]']").click()
    nameofproduct = 'Test_product'
    driver.find_element_by_xpath("//input[@name='name[en]']").send_keys(nameofproduct)
    driver.find_element_by_xpath("//input[@name='code']").click()
    driver.find_element_by_xpath("//input[@name='code']").send_keys('2345')
    driver.find_element_by_xpath("//input[@value='1-2']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//input[@name='quantity']").click()
    driver.find_element_by_xpath("//input[@name='quantity']").clear()
    driver.find_element_by_xpath("//input[@name='quantity']").send_keys('1')
    time.sleep(1)
    image = driver.find_element_by_xpath("//input[@type='file']")
    image.send_keys(os.getcwd() + "/test.jpeg")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='date_valid_from']").click()
    driver.find_element_by_name('date_valid_from').send_keys('2018-04-10')
    driver.find_element_by_xpath("//input[@name='date_valid_to']").click()

    #information

    driver.find_element_by_xpath("//a[@href='#tab-information']").click()
    time.sleep(5)
    select = Select(driver.find_element_by_name("manufacturer_id"))
    select.select_by_visible_text("ACME Corp.")

    driver.find_element_by_xpath("//input[@name='short_description[en]']").click()
    driver.find_element_by_xpath("//input[@name='short_description[en]']").send_keys('very short description of this product')

    driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").click()
    driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").send_keys('not that short description but shorter than short')

    driver.find_element_by_xpath("//input[@name='head_title[en]']").click()
    driver.find_element_by_xpath("//input[@name='head_title[en]']").send_keys('test')

    driver.find_element_by_xpath("//input[@name='meta_description[en]']").click()
    driver.find_element_by_xpath("//input[@name='meta_description[en]']").send_keys('test')

    #prices

    driver.find_element_by_xpath("//a[@href='#tab-prices']").click()
    time.sleep(5)

    driver.find_element_by_xpath("//input[@name='purchase_price']").click()
    driver.find_element_by_xpath("//input[@name='purchase_price']").clear()
    driver.find_element_by_xpath("//input[@name='purchase_price']").send_keys('10')

    select1 = Select(driver.find_element_by_name("purchase_price_currency_code"))
    select1.select_by_visible_text("US Dollars")

    driver.find_element_by_xpath("//input[@name='prices[USD]']").click()
    driver.find_element_by_xpath("//input[@name='prices[USD]']").send_keys('10')

    driver.find_element_by_xpath("//input[@name='prices[EUR]']").click()
    driver.find_element_by_xpath("//input[@name='prices[EUR]']").send_keys('10')

    time.sleep(1)

    driver.find_element_by_xpath("//input[@name='gross_prices[USD]']").click()
    driver.find_element_by_xpath("//input[@name='gross_prices[USD]']").clear()
    driver.find_element_by_xpath("//input[@name='gross_prices[USD]']").send_keys('1')

    driver.find_element_by_xpath("//input[@name='gross_prices[EUR]']").click()
    driver.find_element_by_xpath("//input[@name='gross_prices[EUR]']").clear()
    driver.find_element_by_xpath("//input[@name='gross_prices[EUR]']").send_keys('1')

    driver.find_element_by_name('save').click()
    time.sleep(1)

    driver.find_element_by_xpath("//input[@type='search']").click()
    driver.find_element_by_xpath("//input[@type='search']").send_keys(nameofproduct)

    driver.find_element_by_xpath("//i[@class='fa fa-check-square-o fa-fw checkbox-toggle']").click()
    driver.find_element_by_xpath("//button[@name='enable']").click()

    time.sleep(1)

    rows = driver.find_elements_by_xpath("//tr[@class='row']")
    product = []
    for elements in rows:
        column = elements.find_elements_by_tag_name("td")
        product.append(column[2].find_element_by_tag_name("a").get_attribute("textContent"))

    print(product)

    assert product.__contains__(nameofproduct)









