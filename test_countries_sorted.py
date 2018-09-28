#Сделайте сценарии, которые проверяют сортировку стран и геозон (штатов) в учебном приложении litecart.
#1) на странице http://localhost/litecart/admin/?app=countries&doc=countries
#а) проверить, что страны расположены в алфавитном порядке
#б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке
#
#2) на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
#зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке

import pytest
import time
from selenium import webdriver
from driver_fixture import *

def login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()


def quit(driver):
    driver.quit()

def test_sorted_countries(driver):
    login(driver)
    driver.find_element_by_xpath("//span[text()='Countries']").click()
    countries = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a")
    list=[]
    for country in countries:
        print(country.get_attribute('href'))
    list.append(country.get_attribute('href'))
    
    sorted_list = sorted(list)

    assert list == sorted_list



    #driver.find_element_by_xpath("//span[text()='Countries']").click()
    #rows=driver.find_elements_by_xpath("//tr[@class='row']//a")
    #rows=[]
    #for row in rows:
    #    row.find_elements_by_xpath("//tr[@class='row']//a")
    #    print(rows[row])
#


    #for row in rows:
    #    countries = row.find_elements_by_xpath("//tr[@class='row']//a")
    #    print(countries[0])
#







