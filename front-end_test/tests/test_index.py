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

def test_signin_button(browser):
    browser.get('http://localhost:8000/index.html')
    signin_button = browser.find_element(By.CSS_SELECTOR, 'button.btn--primary')
    signin_button.click()
    WebDriverWait(browser, 10).until(EC.url_contains('main.html'))
    assert 'main.html' in browser.current_url  # 断言导航到主页面

def test_signup_button(browser):
    browser.get('http://localhost:8000/index.html')
    signup_button = browser.find_element(By.CSS_SELECTOR, 'button.btn:nth-child(2)')
    signup_button.click()
    WebDriverWait(browser, 10).until(EC.url_contains('agreement.html'))
    assert 'agreement.html' in browser.current_url  # 断言导航到协议页面

def test_administer_link(browser):
    browser.get('http://localhost:8000/index.html')
    administer_link = browser.find_element(By.CSS_SELECTOR, 'a.btn--text')
    administer_link.click()
    WebDriverWait(browser, 10).until(EC.url_contains('scan-qr-patient.html'))
    assert 'scan-qr-patient.html' in browser.current_url  # 断言导航到扫描患者二维码页面