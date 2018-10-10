import pytest
import time
from selenium import webdriver
from driver_fixture import *

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

#Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
#
#1) открыть главную страницу
#2) открыть первый товар из списка
#2) добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
#3) подождать, пока счётчик товаров в корзине обновится
#4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
#5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
#6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица


def three_items(driver):
    #добавляем три товара
    driver.get("http://litecart.stqa.ru/en/")
    time.sleep(2)
    driver.find_element_by_xpath(".//li[@class='product column shadow hover-light']").click()
    try:
        present = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='options[Size]']")))
        if present:
            WebDriverWait(driver, 2).until(
                    EC.presence_of_element_located((By.XPATH, "//select[@name='options[Size]']")))
            select_state = Select(driver.find_element_by_css_selector("select[name='options[Size]']"))
            select_state.select_by_visible_text("Small")
    except TimeoutException:
        print ("nothing is here")

    time.sleep(1)
    quantity = driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/checkout']//span[@class='quantity']").get_attribute('textContent')
    plusitem = int(quantity) + 1
    allitems = str(plusitem)
    print(quantity)
    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
    wait = WebDriverWait(driver, 2)
    wait.until(EC.text_to_be_present_in_element((By.XPATH,"//a[@href='http://litecart.stqa.ru/en/checkout']//span[@class='quantity']"), allitems))
    new_quantity = driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/checkout']//span[@class='quantity']").get_attribute('textContent')
    assert allitems == new_quantity
    print(new_quantity)
    driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/']").click()

def test_three_items(driver):
    three_items(driver)
    three_items(driver)
    three_items(driver)
    deleting(driver)


def deleting(driver):
    driver.get("http://litecart.stqa.ru/en/checkout")
    # проверяем таблицу для удаления
    table = driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']")
    len_table = len(table)
    print("Total " + str(len(table)))

    while True:
            print("something")

            new_len_table = 0
            try:
                driver.find_element_by_name("remove_cart_item").click()
                time.sleep(5)
                new_len_table = len(driver.find_elements_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td[@class='unit-cost']"))
            except:
                new_len_table = 0

            assert len_table == new_len_table + 1
            len_table = new_len_table

            if len_table == 0:
                break














































