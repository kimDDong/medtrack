import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_check_duplicate(browser):
    browser.get('http://localhost:8000/signup.html')

    username_input = browser.find_element(By.ID, 'register-username')
    username_input.send_keys('existingUser')

    check_duplicate_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="checkDuplicate()"]')
    check_duplicate_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == "이미 존재하는 아이디입니다."
    alert.accept()

    username_input.clear()
    username_input.send_keys('newUser')
    check_duplicate_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == "사용 가능한 아이디입니다."
    alert.accept()

def test_search_zipcode_address(browser):
    browser.get('http://localhost:8000/signup.html')

    zipcode_input = browser.find_element(By.ID, 'register-zipcode')
    zipcode_input.send_keys('12345')

    search_zipcode_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="searchZipcode(\'address\')"]')
    search_zipcode_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == "주소를 검색합니다."
    alert.accept()

def test_search_zipcode_hospital(browser):
    browser.get('http://localhost:8000/signup.html')

    zipcode_input = browser.find_element(By.ID, 'hospital-zipcode')
    zipcode_input.send_keys('12345')

    search_zipcode_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="searchZipcode(\'hospital\')"]')
    search_zipcode_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == "병원 주소를 검색합니다."
    alert.accept()