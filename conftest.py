import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LOGIN_BUTTON, EMAIL_FIELD, PASSWORD_FIELD, SUBMIT_LOGIN_BUTTON, PROFILE_NAME


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://qa-desk.education-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def logged_in_driver(driver):
    driver.find_element(*LOGIN_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(EMAIL_FIELD)).send_keys("imkliuchi@mail.com")
    driver.find_element(*PASSWORD_FIELD).send_keys("1234")
    driver.find_element(*SUBMIT_LOGIN_BUTTON).click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PROFILE_NAME))
    return driver
