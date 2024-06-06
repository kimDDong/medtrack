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

def test_start_scanning(browser):
    browser.get('http://localhost:8000/scan-qr-patient.html')

    start_scanning_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="startScanning(\'scan\')"]')
    start_scanning_button.click()

    assert 'QR 코드 스캔하기' in browser.page_source

def test_navigate_back(browser):
    browser.get('http://localhost:8000/patient-info.html')
    
    browser.get('http://localhost:8000/scan-qr-patient.html')
    
    back_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn--secondary')
    back_button.click()
    
    WebDriverWait(browser, 10).until(EC.url_contains('patient-info.html'))
    assert 'patient-info.html' in browser.current_url  # 断言返回到了之前访问的主页面