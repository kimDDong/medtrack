# test_change_notification_sound.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome() 
    yield driver
    driver.quit()

def test_page_title(driver):
    driver.get("http://localhost:8000/change-notification-sound.html")
    assert driver.title == "알림 목소리 변경"

def test_heading_exists(driver):
    driver.get("http://localhost:8000/change-notification-sound.html")
    heading = driver.find_element(By.CSS_SELECTOR, "h2")
    assert heading.text == "알림 목소리 변경"

def test_sound_list_exists(driver):
    driver.get("http://localhost:8000/change-notification-sound.html")
    sound_list = driver.find_element(By.ID, "soundList")
    assert sound_list is not None

def test_record_button_exists(driver):
    driver.get("http://localhost:8000/change-notification-sound.html")
    record_button = driver.find_element(By.CSS_SELECTOR, ".sound-actions .btn--primary")
    assert record_button is not None
    assert record_button.get_attribute("onclick") == "recordSound()"

def test_upload_button_exists(driver):
    driver.get("http://localhost:8000/change-notification-sound.html")
    upload_button = driver.find_element(By.CSS_SELECTOR, ".sound-actions .btn--primary:nth-of-type(2)")
    assert upload_button is not None
    assert upload_button.get_attribute("onclick") == "document.getElementById('uploadSound').click()"

def test_back_button_exists(driver):
    driver.get("http://localhost:8000/change-notification-sound.html")
    back_button = driver.find_element(By.CSS_SELECTOR, ".btn--secondary")
    assert back_button is not None
    assert back_button.get_attribute("onclick") == "navigateBack()"