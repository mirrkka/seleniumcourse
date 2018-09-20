import os
import pytest
from selenium import webdriver


@pytest.fixture()
def driver(request):
    driver_object = webdriver.Chrome(os.path.abspath(os.path.join(os.path.dirname(__file__), 'drivers\\chromedriver.exe')))

    def resource_teardown():
        driver_object.quit()
    request.addfinalizer(resource_teardown)

    return driver_object

