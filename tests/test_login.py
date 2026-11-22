from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (LOGIN_BUTTON, EMAIL_FIELD, PASSWORD_FIELD, SUBMIT_LOGIN_BUTTON, PROFILE_BUTTON, PROFILE_NAME)


def test_login(driver):
    driver.find_element(*LOGIN_BUTTON).click()
    driver.find_element(*EMAIL_FIELD).send_keys("imkliuchi@mail.com")
    driver.find_element(*PASSWORD_FIELD).send_keys("test1234")
    driver.find_element(*SUBMIT_LOGIN_BUTTON).click()

    assert WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON)).is_displayed()

    assert "User" in WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PROFILE_NAME)).text
