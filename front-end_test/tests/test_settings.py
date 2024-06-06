import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_change_font_size(browser):
    browser.get('http://localhost:8000/settings.html')

    font_size_select = Select(browser.find_element(By.ID, 'font-size'))
    font_size_select.select_by_value('1.5rem')

    font_size_style = browser.find_element(By.TAG_NAME, 'html').get_attribute('style')
    assert '--font-size: 1.5rem;' in font_size_style

def test_change_password(browser):
    browser.get('http://localhost:8000/settings.html')

    new_password_input = browser.find_element(By.ID, 'new-password')
    new_password_input.send_keys('newpassword')

    change_password_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="changePassword()"]')
    change_password_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == '비밀번호가 변경되었습니다.'
    alert.accept()

def test_delete_account(browser):
    browser.get('http://localhost:8000/settings.html')

    delete_account_button = browser.find_element(By.CSS_SELECTOR, 'button[onclick="deleteAccount()"]')
    delete_account_button.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == '정말로 회원 탈퇴를 하시겠습니까?'
    alert.accept()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == '회원 탈퇴가 완료되었습니다.'
    alert.accept()

def test_toggle_voice_assist(browser):
    browser.get('http://localhost:8000/settings.html')

    voice_assist_checkbox = browser.find_element(By.ID, 'voice-assist')
    voice_assist_checkbox.click()

    alert = WebDriverWait(browser, 10).until(EC.alert_is_present())
    assert alert.text == '음성 보조가 활성화되었습니다.'
    alert.accept()

def test_navigate_back(browser):
    browser.get('http://localhost:8000/main.html')

    browser.get('http://localhost:8000/settings.html')
    
    back_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn--secondary')
    back_button.click()
    
    WebDriverWait(browser, 10).until(EC.url_contains('main.html'))
    assert 'main.html' in browser.current_url