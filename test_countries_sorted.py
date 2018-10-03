
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

#Сделайте сценарии, которые проверяют сортировку стран и геозон (штатов) в учебном приложении litecart.
#1) на странице http://localhost/litecart/admin/?app=countries&doc=countries
#а) проверить, что страны расположены в алфавитном порядке
#б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке

def test_sorted_countries(driver):
    login(driver)
    driver.find_element_by_xpath("//span[text()='Countries']").click()
    country_list = []
    notzero=[]
    rows = driver.find_elements_by_xpath(".//table[@class='dataTable']//tr[@class='row']")
    for elements in rows:
        column = elements.find_elements_by_tag_name("td")
        country_list.append(column[4].text)
        if int(column[5].text) > 0:
            notzero.append(column[4].find_element_by_tag_name("a").get_attribute("href"))


    sorted_countries = sorted(country_list)
    assert sorted_countries == country_list

    for country_link in notzero:
        driver.get(country_link)
        zones = []
        row = driver.find_elements_by_css_selector("table#table-zones tr:not([class=header])")
        for element in row:
            column = element.find_elements_by_tag_name("td")
            zones.append(column[2].text)
        zones.pop()

        print(zones)

        sorted_zones = sorted(zones)
        assert sorted_zones == zones

        driver.back()


#2) на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
#зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке

def test_geozones(driver):
    login(driver)
    driver.find_element_by_xpath("//span[text()='Geo Zones']").click()
    geozones = []
    links = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a")
    for link in links:
        print(link.get_attribute('href'))
        geozones.append(link.get_attribute('href'))
    print(geozones)

    for i in geozones:
        driver.get(i)
        zones1 = []
        selects = driver.find_elements_by_xpath(".//*[@id='table-zones']/tbody/tr/td/select[starts-with(@name,'zones[') and not(contains (@aria-hidden,'true'))]/option[@selected='selected']")
        for things in selects:
            zones1.append(things.get_attribute("textContent"))

        print(zones1)
        sorted_zones = sorted(zones1)
        assert sorted_zones == zones1
        driver.back()



















#2) на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
#зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке

#def test_sorted_geo_zones(driver):
#    login(driver)
#    driver.find_element_by_xpath("//span[text()='Geo Zones']").click()
#    geolinks=[]
#    geo = driver.find_elements_by_xpath(".//*[@id='content']/form/table/tbody/tr[@class='row']/td [not(contains (@style,'text'))]/a")
#    for zone in geo:
#        print(zone.get_attribute('href'))
#        geolinks.append(zone.get_attribute('href')) # запоминаем ссылки в массив, чтобы при переключении и обновлении не протухали ссылки
#        print(geolinks)
#
#    for i in range(len(geolinks)):
#        geozones=[]
#        driver.get(geolinks[i])
#        zones = driver.find_elements_by_xpath(".//table[@class='dataTable']//tr[2]")
#        for k in zones:
#            selected_zones = k.find_elements_by_tag_name("td")
#            geozones.append(selected_zones[3].get_attribute('value'))
#            sorted_geozones = sorted(geozones)
#            assert geozones == sorted_geozones
#






































