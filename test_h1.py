import pytest
import time
from selenium import webdriver
from driver_fixture import *
from selenium.common.exceptions import NoSuchElementException

def login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()
    #driver.quit()


def test_h1(driver):
    login(driver)
    driver.find_element_by_xpath("//span[text()='Appearence']").click()
    driver.find_element_by_xpath("//li[@id='doc-template']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-logotype']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Catalog']").click()
    driver.find_element_by_xpath("//li[@id='doc-catalog']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-product_groups']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-option_groups']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-manufacturers']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-suppliers']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-delivery_statuses']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-sold_out_statuses']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-quantity_units']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-csv']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//li[@id='doc-quantity_units']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0
    time.sleep(1)


    driver.find_element_by_xpath("//span[text()='Countries']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Currencies']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Customers']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-csv']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-newsletter']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Geo Zones']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Languages']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-storage_encoding']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Modules']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-customer']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-shipping']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-payment']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-order_total']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-order_success']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-order_action']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Orders']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-order_statuses']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Pages']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Reports']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-most_sold_products']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-most_shopping_customers']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    time.sleep(1)

    driver.find_element_by_xpath("//span[text()='Settings']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-defaults']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-general']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-listings']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-images']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-checkout']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-advanced']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-security']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//span[text()='Slides']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//span[text()='Tax']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-tax_rates']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//span[text()='Translations']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-scan']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//li[@id='doc-csv']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//span[text()='Users']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

    driver.find_element_by_xpath("//span[text()='vQmods']").click()
    assert len(driver.find_elements_by_tag_name('h1')) > 0

























