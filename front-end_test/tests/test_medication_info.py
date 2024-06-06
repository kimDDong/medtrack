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

def test_generate_qr_code(browser):
    browser.get('http://localhost:8000/medication-info.html')

    generate_qr_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="generateQRCode()"]')
    generate_qr_button.click()

    qr_code = browser.find_element(By.ID, 'qrcode')
    assert qr_code.is_displayed()

def test_navigate_back(browser):
    browser.get('http://localhost:8000/medication-info.html')

    back_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="navigateBack()"]')
    back_button.click()

    assert 'medication-info.html' in browser.current_url