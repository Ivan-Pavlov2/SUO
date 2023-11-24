import pytest
from selenium import webdriver
import data
from selenium.webdriver.common.by import By

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get('https://suo.royalsw.me/sections/list?page=1')
    driver.implicitly_wait(5)
    driver.find_element( By.ID, "username").send_keys(data.email)
    driver.find_element( By.ID, "password").send_keys(data.password)
    driver.find_element( By.ID, "kc-login").click()
    yield driver
    driver.quit()
