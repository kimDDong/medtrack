import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_agree_button(browser):
    browser.get('http://localhost:8000/agreement.html')

    agree_button = browser.find_element(By.CSS_SELECTOR, 'button.btn--primary')
    agree_button.click()

    # 进行断言以验证预期结果
    assert 'signup.html' in browser.current_url

def test_cancel_button(browser):
    browser.get('http://localhost:8000/agreement.html')

    cancel_button = browser.find_element(By.CSS_SELECTOR, 'button.btn--secondary')
    cancel_button.click()

    # 进行断言以验证预期结果
    assert 'index.html' in browser.current_url