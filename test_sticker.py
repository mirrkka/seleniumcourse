import pytest
import time
from selenium import webdriver
from driver_fixture import *

#Сделайте сценарий, проверяющий наличие стикеров у всех товаров в учебном приложении litecart на главной странице.
# Стикеры -- это полоски в левом верхнем углу изображения товара, на которых написано New или Sale или что-нибудь другое.
# Сценарий должен проверять, что у каждого товара имеется ровно один стикер.

def test_sticker_on(driver):
    driver.get("http://localhost/litecart")
    time.sleep(3)

    products = driver.find_elements_by_xpath("//div[@class='image-wrapper']")
    print("There are " + str(len(products)) + " ducks")

    for one in products:
        stickers = one.find_elements_by_xpath("//div[starts-with(@class,'sticker')]")
        print ("There are " + str(len(stickers)) + " stickers")

    assert len(products) == len(stickers)




















