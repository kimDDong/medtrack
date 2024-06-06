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

def test_page_title(browser):
    browser.get('http://localhost:8000/display-medication.html')
    assert '약물 정보' in browser.title

def test_qr_code_scan_section(browser):
    browser.get('http://localhost:8000/display-medication.html')
    assert '환자 이름:' in browser.page_source
    assert '내원 일자:' in browser.page_source

def test_medication_section(browser):
    browser.get('http://localhost:8000/display-medication.html')
    medication_section = browser.find_element(By.ID, 'medications')
    assert medication_section.is_displayed()
    assert '약물 정보' in medication_section.text

def test_add_medication_button(browser):
    browser.get('http://localhost:8000/display-medication.html')
    add_medication_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn--primary')
    assert add_medication_button.is_displayed()
    assert '약물 추가하기' in add_medication_button.text

    add_medication_button.click()
    WebDriverWait(browser, 10).until(EC.url_contains('add-medication.html'))
    assert 'add-medication.html' in browser.current_url

def test_back_button(browser):
    browser.get('http://localhost:8000/display-medication.html')
    back_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn--secondary')
    assert back_button.is_displayed()
    assert '뒤로가기' in back_button.text

    back_button.click()
    WebDriverWait(browser, 10).until(EC.url_contains('main.html'))
    assert 'main.html' in browser.current_url