import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_patient_name(browser):
    browser.get('http://localhost:8000/patient-info.html')

    patient_name = browser.find_element(By.ID, 'patientName')
    assert '김동현' in patient_name.text


def test_save_patient_info(browser):
    browser.get('http://localhost:8000/patient-info.html')
    save_patient_info_button = browser.find_element(By.CSS_SELECTOR, '.info-actions .btn--primary:nth-child(1)')
    save_patient_info_button.click()

    # 等待警告框出现并处理它
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = Alert(browser)
    assert alert.text == '환자 정보가 저장되었습니다.'
    alert.accept()

def test_load_patient_info(browser):
    browser.get('http://localhost:8000/patient-info.html')
    load_patient_info_button = browser.find_element(By.CSS_SELECTOR, '.info-actions .btn--primary:nth-child(2)')
    load_patient_info_button.click()

    # 等待警告框出现并处理它
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = Alert(browser)
    assert alert.text == '환자 정보가 불러와졌습니다.'
    alert.accept()


def test_navigate_back(browser):
    # 先导航到一个已知页面,例如主页面
    browser.get('http://localhost:8000/main.html')
    
    # 然后导航到患者信息页面
    browser.get('http://localhost:8000/patient-info.html')
    
    back_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn--secondary')
    back_button.click()
    
    WebDriverWait(browser, 10).until(EC.url_contains('main.html'))
    assert 'main.html' in browser.current_url  # 断言返回到了之前访问的主页面