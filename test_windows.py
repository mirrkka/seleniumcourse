
import pytest
import time
from selenium import webdriver
from driver_fixture import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from contextlib import contextmanager

def login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()

@contextmanager
def wait_for_new_window(driver, timeout=10): #http://stackoverflow.com/questions/26641779/python-selenium-how-to-wait-for-new-window-opens
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))


def test_about_windows(driver):
    login(driver)
    driver.find_element_by_xpath("//a[@href='http://localhost/litecart/admin/?app=countries&doc=countries']").click()
    driver.find_element_by_xpath(".//*[@id='content']/div/a").click()
    all_links = driver.find_elements_by_xpath(".//*[@id='content']/form/table[1]//a[@target='_blank']")
    print(str(len(all_links)))

    main_window = driver.current_window_handle
    print(main_window)

    old_windows = driver.window_handles
    print(old_windows)
    for i in range (len(all_links)):
        print(str(i))
        with wait_for_new_window(driver, 10):
            all_links[i].click()

        new_windows = driver.window_handles
        print(new_windows)

        new_window = list(set(new_windows).difference(old_windows))
        print(new_window)

        driver.switch_to_window(new_window[0])
        driver.close()
        driver.switch_to_window(main_window)




#main_window = driver.current_window_handle
#old_windows = driver.window_handles
#link.click() # открывает новое окно
## ожидание появления нового окна,
## идентификатор которого отсутствует в списке oldWindows,
## остаётся в качестве самостоятельного упражнения
#new_window = wait.until(there_is_window_other_than(old_windows))
#driver.switch_to_window(new_window)
## ...
#driver.close()
#driver.switch_to_window(main_window)