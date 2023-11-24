import pytest
from selenium import webdriver
import data

@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=options)
    driver.get('https://suo.royalsw.me/sections/list?page=1')
    driver.find_element('By.NAME, "username"').send_keys(data.email)
    driver.find_element('By.NAME, "password"').send_keys(data.password)
    driver.find_element('By.NAME, "login"').click()
    yield driver
    driver.quit()
