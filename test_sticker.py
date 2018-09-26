import pytest
import time
from selenium import webdriver
from driver_fixture import *

def test_sticker_on(driver):
    driver.get("http://localhost/litecart/admin/")