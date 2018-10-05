import pytest
import time
from selenium import webdriver
from driver_fixture import *

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

#Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.
#
#1) открыть главную страницу
#2) открыть первый товар из списка
#2) добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
#3) подождать, пока счётчик товаров в корзине обновится
#4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
#5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
#6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица

def login(driver):
    driver.get("http://litecart.stqa.ru/en/")

def test_three_items(driver):
    #добавляем три товара
    login(driver)
    time.sleep(5)
    for i in range(1,4):
      items = driver.find_elements_by_xpath("//a[@class='listing-wrapper products']//li")
      #print(str(len(items)))
    for k in items:
        k.find_element_by_xpath("./a[@class='link']").click()
        driver.find_element_by_xpath("//button[@name='add_cart_product']").click()



#    time.sleep(5)
#    quantity = driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/checkout']//span[@class='quantity']").get_attribute('textContent')
#    plusitem = int(quantity) + 1
#    allitems = str(plusitem)
#    print(quantity)
#    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
#    wait = WebDriverWait(driver, 5)
#    wait.until(EC.text_to_be_present_in_element((By.XPATH,"//a[@href='http://litecart.stqa.ru/en/checkout']//span[@class='quantity']"), allitems))
#    new_quantity = driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/checkout']//span[@class='quantity']").get_attribute('textContent')
#
#    assert allitems == new_quantity
#    print(new_quantity)
#    driver.find_element_by_xpath("//a[@href='http://litecart.stqa.ru/en/']").click()
#
#
#def deleting(driver):
#    # проверяем таблицу для удаления
#    quantity1 = driver.find_element_by_xpath(".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td").get_attribute('textContent')
#    minus = int(quantity1) - 1
#    afterdelete = str(minus)
#    print(afterdelete)
#
#    # убираем товар из корзины
#
#    driver.find_element_by_xpath("//input[@type='number']").click()
#    driver.find_element_by_xpath("//input[@type='number']").clear()
#    driver.find_element_by_xpath("//input[@type='number']").send_keys(minus)
#    driver.find_element_by_xpath("//button[@name='update_cart_item']").click()
#
#    # смотрим, что там в таблице
#
#    wait = WebDriverWait(driver, 5)
#    wait.until(EC.text_to_be_present_in_element((By.XPATH, ".//*[@id='order_confirmation-wrapper']/table/tbody/tr/td"), afterdelete))
#    new_quantity1 = driver.find_element_by_xpath("//table[@class='dataTable rounded-corners']//td").get_attribute('textContent')
#
#    assert afterdelete == new_quantity1
#    print(new_quantity1)
















