import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_add_medication_form(browser):
    browser.get('http://localhost:8000/add-medication.html')

    # Wait for the medication name input element to be visible and present
    medication_name_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'medicationName'))
    )
    medication_name_input.send_keys('Aspirin')

    # Wait for the known medication select element to be visible and present
    known_medication_select = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'knownMedication'))
    )
    known_medication_select.send_keys('no')

    # Wait for the disease input element to be visible and interactable
    disease_input = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.ID, 'disease'))
    )
    disease_input = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'disease'))
    )
    disease_input.send_keys('Headache')

    # Wait for the color input element to be visible and present
    color_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'color'))
    )
    color_input.send_keys('White')

    # Wait for the submit button to be clickable
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]'))
    )
    submit_button.click()

    # Wait for the success message or any indication of successful submission
    success_message = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
    )
    assert '약물 추가' in success_message.text