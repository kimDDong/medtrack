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

def test_greeting(browser):
    browser.get('http://localhost:8000/main.html')

    greeting = browser.find_element(By.ID, 'greeting')
    assert '안녕하세요, 김동현님' in greeting.text

def test_navigate_to_settings(browser):
    browser.get('http://localhost:8000/main.html')

    settings_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="navigateTo(\'settings\')"]')
    settings_button.click()

    assert 'settings.html' in browser.current_url

def test_navigate_to_scan(browser):
    browser.get('http://localhost:8000/main.html')
    scan_button = browser.find_element(By.CSS_SELECTOR, '.header-buttons .btn--secondary:nth-child(2)')
    scan_button.click()
    WebDriverWait(browser, 10).until(EC.url_contains('medication-info.html'))
    assert 'medication-info.html' in browser.current_url 

def test_navigate_to_send_medication_info(browser):
    browser.get('http://localhost:8000/main.html')
    send_medication_info_button = browser.find_element(By.CSS_SELECTOR, '.btn-group .btn--primary:nth-child(1)')
    send_medication_info_button.click()
    WebDriverWait(browser, 10).until(EC.url_contains('scan-qr.html'))
    assert 'scan-qr.html' in browser.current_url 

def test_navigate_to_change_voice(browser):
    browser.get('http://localhost:8000/main.html')
    change_voice_button = browser.find_element(By.CSS_SELECTOR, '.btn-group .btn--primary:nth-child(3)')
    change_voice_button.click()
    WebDriverWait(browser, 10).until(EC.url_contains('change-notification-sound.html'))
    assert 'change-notification-sound.html' in browser.current_url  

def test_navigate_to_add_medication(browser):
    browser.get('http://localhost:8000/main.html')

    add_medication_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="navigateTo(\'addMedication\')"]')
    add_medication_button.click()

    assert 'add-medication.html' in browser.current_url
