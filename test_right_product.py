import pytest
import time
from selenium import webdriver
from driver_fixture import *
import re
import ast

#а) на главной странице и на странице товара совпадает текст названия товара
#б) на главной странице и на странице товара совпадают цены (обычная и акционная)
#в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
#г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
#(цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
#д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)

def test_product(driver):
    driver.get("http://localhost/litecart")
    time.sleep(3)
    duck = driver.find_elements_by_xpath("//div[@id='box-campaigns']//li[@class='product column shadow hover-light']")


    link_product=[]

    name = []
    regular_price = []
    reduced_price = []
    reduced_price_tag = []
    regular_price_style_text_decoration = []
    regular_price_style_font_size = []
    reduced_price_style_font_weight = []
    reduced_price_style_font_size = []

    for elements in duck:
        link_product.append((elements.find_element_by_xpath(".//a[@class='link']").get_attribute('href')))
        name.append(elements.find_element_by_xpath(".//div[@class='name']").get_attribute('textContent'))
        regular_price.append(elements.find_element_by_xpath(".//div[@class='price-wrapper']/s").get_attribute('textContent'))
        reduced_price.append(elements.find_element_by_xpath(".//div[@class='price-wrapper']/strong").get_attribute('textContent'))
        reduced_price_tag.append(elements.find_element_by_xpath(".//div[@class='price-wrapper']/strong").get_attribute('tagName'))
        regular_price_style_text_decoration.append(elements.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('text-decoration'))
        regular_price_style_font_size.append(elements.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('font-size'))
        reduced_price_style_font_weight.append(elements.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight'))
        reduced_price_style_font_size.append(elements.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-size'))

    print(name)
    print(regular_price)
    print(reduced_price)
    print(regular_price_style_text_decoration)
    print(regular_price_style_font_size)
    print(reduced_price_style_font_weight)
    print(reduced_price_style_font_size)
    print(reduced_price_tag)

    for k in range(len(name)):
        driver.get(link_product[k])
        a_name = driver.find_element_by_xpath(".//*[@id='box-product']/div[1]/h1").get_attribute('textContent')
        a_regular_price = driver.find_element_by_xpath("//s[@class='regular-price']").get_attribute('textContent')
        a_reduced_price = driver.find_element_by_xpath("//strong[@class='campaign-price']").get_attribute('textContent')
        a_regular_price_style_text_decoration = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('text-decoration')
        a_regular_price_style_font_size = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('font-size')
        a_reduced_price_style_font_weight = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')
        a_reduced_price_style_font_size = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-size')
        a_reduced_price_tag = driver.find_element_by_xpath("//strong[@class='campaign-price']").get_attribute('tagName')
        a_regular_price_style_text_decoration_color = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('color')
        rgba = a_regular_price_style_text_decoration_color
        r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
        hex_value = '#%02x%02x%02x' % (r, g, b)
        a_reduced_price_style_color = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('color')
        rgba = a_reduced_price_style_color
        r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
        hex = '#%02x%02x%02x' % (r, g, b)

        print(hex)
        print(hex_value)
        print(a_name)
        print(a_regular_price)
        print(a_reduced_price)
        print(a_regular_price_style_text_decoration)
        print(a_regular_price_style_font_size)
        print(a_reduced_price_style_font_weight)
        print(a_reduced_price_style_font_size)
        print(a_regular_price_style_text_decoration_color)


    assert name[k] == a_name #а) на главной странице и на странице товара совпадает текст названия товара
    assert regular_price[k] == a_regular_price #б) на главной странице и на странице товара совпадают цены (обычная и акционная)
    assert reduced_price[k] == a_reduced_price #б) на главной странице и на странице товара совпадают цены (обычная и акционная)
    assert regular_price_style_text_decoration[k] != a_regular_price_style_text_decoration
    assert regular_price_style_font_size[k] < a_regular_price_style_font_size #акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)
    assert reduced_price_tag ==['STRONG'] # проверка жирного шрифта по тегу
    assert a_reduced_price_tag == 'STRONG'  # проверка жирного шрифта по тегу
    assert (reduced_price_style_font_weight[k] == a_reduced_price_style_font_weight) > (regular_price_style_font_size[k] == a_regular_price_style_font_size)
    assert regular_price_style_text_decoration[k].__contains__("line-through solid rgb(119, 119, 119)") #проверка зачеркивания цены (наличие line-through)
    assert a_regular_price_style_text_decoration.__contains__("line-through solid rgb(102, 102, 102)") #проверка зачеркивания цены (наличие line-through)
    assert hex_value == '#666666' #проверка серого цвета обычной цены на странице товара
    assert hex == '#cc0000' #проверка красного цвета акционной цены на странице товара


def test_product_color(driver):
    driver.get("http://localhost/litecart")
    time.sleep(3)
    color = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('color')
    rgba = color
    r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
    hex2 = '#%02x%02x%02x' % (r, g, b)
    color2 = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('color')
    rgba = color2
    r, g, b, alpha = ast.literal_eval(rgba.strip("rgba"))
    hex3 = '#%02x%02x%02x' % (r, g, b)
    print(hex2)
    print(hex3)

    assert hex2 == '#777777' # проверка обычного цвета на общей странице
    assert hex3 == 'cc0000' # проверка красного цвета на общей странице





















