import pytest
import time
from selenium import webdriver
from driver_fixture import *

#def login(driver):
#    driver.get("http://localhost/litecart/admin/")
#    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
#    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
#    driver.find_element_by_xpath("//button[@name='login']").click()
#    driver.quit()
#
#
#def test_login(driver):
#    login(driver)

import re

with open("C:\\Users\\a.ryzhkova\\Downloads\\dataset_3363_2 (4).txt",'r+') as f:
    a = re.split(r"(\d+)",f.readline())[:-1]
    result = ''.join([y * int(x) for x,y in zip(a[1::2],a[::2])])
    print(result)
    f.seek(0)
    f.write(result)

   # with open('dataset_3363_2.txt', 'r') as f:
   #     s = f.readline().strip()
   # i = 0
   # while i < len(s):
   #     j = i + 1
   #     while j < len(s) and s[j].isdigit()
   #         j += 1
   #     print(s[i] * int(s[i + 1:j]), end='')
   #     i = j


import re
with open("C:\\Users\\a.ryzhkova\\Downloads\\dataset_3363_2 (4).txt") as file:
    t = file.readline()
for i in re.compile(r"(\w)(\d+)").finditer(t):
    print (i.group(1) * int(i.group(2)), end="")