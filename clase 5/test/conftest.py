import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# set up driver for each test
@pytest.fixture
def driver():
    print("opening chrome driver")
    my_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    yield my_driver

    print("closing chrome driver")
    my_driver.close()
