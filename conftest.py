import pytest
from selenium import webdriver
from data import Data

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.get(Data.SCOOTER_URL)
    yield driver
    driver.quit()
