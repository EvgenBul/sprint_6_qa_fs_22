import pytest
from selenium import webdriver
from data import TestData

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(TestData.scooter_address)
    yield driver
    driver.quit()