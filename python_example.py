import pytest
import time
from selenium import webdriver
from driver_fixture import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


#@pytest.fixture()
#def driver(request):
#    wd = webdriver.Chrome(os.path.abspath(os.path.join(os.path.dirname(__file__), 'drivers\\chromedriver.exe')))
#
#    def resource_teardown():
#        wd.quit()
#    request.addfinalizer(resource_teardown)
#
#    return wd


#def login(driver):
#    driver.get("http://open-eshop.stqa.ru/")
#    driver.find_element_by_xpath("//div[@class='btn-group pull-right btn-header-group']").click()
#    time.sleep(2)
#    driver.find_element_by_xpath("//input[@name='email']").send_keys("demo@open-eshop.com")
#    driver.find_element_by_xpath("//input[@name='password']").send_keys("demo")
#    driver.find_element_by_xpath("//button[@type='submit']").click()
#    driver.find_element_by_xpath("//a[@data-toggle='dropdown']").click()
#    driver.find_element_by_xpath("//i[@class='glyphicon glyphicon-shopping-cart']").click()
#
#def logout(driver):
#    driver.find_element_by_xpath("//a[@data-toggle='dropdown']").click()
#    driver.find_element_by_xpath("//i[@class='glyphicon glyphglyphicon glyphicon-off']").click()
#
#
#def test_login(driver):
#    login(driver)
#    time.sleep(2)
#    assert len(driver.find_elements_by_xpath("//table[@class='table table-striped']//tbody")) != 0
#    time.sleep(1)
#    logout(driver)


from contextlib import contextmanager

@contextmanager #https://docs.python.org/2.7/library/contextlib.html
def wait_for_new_window(driver, timeout=10): #http://stackoverflow.com/questions/26641779/python-selenium-how-to-wait-for-new-window-opens
    handles_before = driver.window_handles
    yield
    WebDriverWait(driver, timeout).until(
        lambda driver: len(handles_before) != len(driver.window_handles))

def test_ext_links(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
    driver.find_element_by_xpath("//input[@name='password']").send_keys("admin")
    driver.find_element_by_xpath("//button[@name='login']").click()
    print()

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_xpath(".//*[@id='content']/div/a").click()
    all_ex_link=driver.find_elements_by_xpath(".//*[@id='content']/form/table[1]//a[@target='_blank']")
    print("Total ext_link: "+ str(len(all_ex_link)))

    # получаем    набор    дескрипторов    текущих    открытых    окон
    main_window = driver.current_window_handle
    print('main_window')
    print(main_window)
    old_windows = driver.window_handles
    print('old_windows')
    print(old_windows)
    # нажимаем    на    ссылку, которая    открывает    документ    в    новом    окне
    #driver.findElement(By.tagName("a")).click();
    for j in range (10):                         #нагрузим
        for i in range (len(all_ex_link)):
            print("i="+str(i))
            with wait_for_new_window(driver,10):
                all_ex_link[i].click()
            #sleep(3)
            # здесь    нужно    будет    дождаться    открытия    нового    окна    \

            # получаем новый    набор    дескрипторов, включающий    уже    и    новое    окно
            new_windows = driver.window_handles
            print('new_windows')
            print(new_windows)
            # получаем     дескриптор    нового    окна (из одного списка вычтем другой)
            new_window = list(set(new_windows).difference(old_windows))
            print('new_window')
            print(new_window)
            #закроем новое окно
            driver.switch_to_window(new_window[0])
            driver.close()
            driver.switch_to_window(main_window)
            #sleep(5)  без слипов на platform win32 -- Python 3.5.2, pytest-3.0.4, py-1.4.31, pluggy-0.4.0 за 16 сек отработало