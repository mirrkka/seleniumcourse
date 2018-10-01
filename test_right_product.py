import pytest
import time
from selenium import webdriver
from driver_fixture import *

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
    regular_price_style_text_decoration = []
    regular_price_style_font_size = []
    reduced_price_style_font_weight = []
    reduced_price_style_font_size = []
    regular_price_style_text_decoration_color = []


    for elements in duck:
        link_product.append((elements.find_element_by_xpath(".//a[@class='link']").get_attribute('href')))
        name.append(elements.find_element_by_xpath(".//div[@class='name']").get_attribute('textContent'))
        regular_price.append(elements.find_element_by_xpath(".//div[@class='price-wrapper']/s").get_attribute('textContent'))
        reduced_price.append(elements.find_element_by_xpath(".//div[@class='price-wrapper']/strong").get_attribute('textContent'))
        regular_price_style_text_decoration.append(elements.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('text-decoration'))
        regular_price_style_text_decoration_color.append(elements.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('color'))
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
    print(regular_price_style_text_decoration_color)



    for k in range(len(name)):
        driver.get(link_product[k])
        a_name = driver.find_element_by_xpath(".//*[@id='box-product']/div[1]/h1").get_attribute('textContent')
        a_regular_price = driver.find_element_by_xpath("//s[@class='regular-price']").get_attribute('textContent')
        a_reduced_price = driver.find_element_by_xpath("//strong[@class='campaign-price']").get_attribute('textContent')
        a_regular_price_style_text_decoration = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('text-decoration')
        a_regular_price_style_text_decoration_color = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('color')
        a_regular_price_style_font_size = driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('font-size')
        a_reduced_price_style_font_weight = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')
        a_reduced_price_style_font_size = driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-size')

        print(a_name)
        print(a_regular_price)
        print(a_reduced_price)
        print(a_regular_price_style_text_decoration)
        print(a_regular_price_style_font_size)
        print(a_reduced_price_style_font_weight)
        print(a_reduced_price_style_font_size)
        print(a_regular_price_style_text_decoration_color)

    assert name[k] == a_name
    assert regular_price[k] == a_regular_price
    assert reduced_price[k] == a_reduced_price
    assert regular_price_style_text_decoration[k] != a_regular_price_style_text_decoration
    assert regular_price_style_font_size[k] < a_regular_price_style_font_size
    assert (reduced_price_style_font_weight[k] == a_reduced_price_style_font_weight) > (regular_price_style_font_size[k] == a_regular_price_style_font_size)
    assert regular_price_style_text_decoration[k].__contains__("line-through solid rgb(119, 119, 119)")
    assert a_regular_price_style_text_decoration.__contains__("line-through solid rgb(102, 102, 102)")
    assert a_regular_price_style_text_decoration_color.__contains__("rgba(102, 102, 102, 1)")
    assert regular_price_style_text_decoration_color.__contains__("rgba(119, 119, 119, 1)")
















