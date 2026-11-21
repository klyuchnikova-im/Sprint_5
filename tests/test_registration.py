import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    LOGIN_BUTTON,
    NO_ACCOUNT_BUTTON,
    EMAIL_FIELD,
    PASSWORD_FIELD,
    CONFIRM_PASSWORD_FIELD,
    CREATE_ACCOUNT_BUTTON,
    PROFILE_NAME,
    PROFILE_BUTTON,
    EMAIL_ERROR
)

class TestRegistration:

    def test_registration(self, driver):
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        email = f"user{random.randint(10000, 99999)}@mail.com"
        password = "test1234"

        driver.find_element(*EMAIL_FIELD).send_keys(email)
        driver.find_element(*PASSWORD_FIELD).send_keys(password)
        driver.find_element(*CONFIRM_PASSWORD_FIELD).send_keys(password)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        avatar = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PROFILE_BUTTON))

        user_name = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(PROFILE_NAME))

        assert avatar.is_displayed()
        assert "User" in user_name.text

class TestRegistrationInvalidEmail:

    def test_registration_invalid_email(self, driver):
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)).click()

        invalid_email = f"user{random.randint(10000, 99999)}@mailcom"

        driver.find_element(*EMAIL_FIELD).send_keys(invalid_email)
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(EMAIL_ERROR))

        assert "Ошибка" in error.text

        email_field = driver.find_element(*EMAIL_FIELD)
        password_field = driver.find_element(*PASSWORD_FIELD)
        confirm_password_field = driver.find_element(*CONFIRM_PASSWORD_FIELD)

        email_parent = email_field.find_element("xpath", "..")
        password_parent = password_field.find_element("xpath", "..")
        confirm_password_parent = confirm_password_field.find_element("xpath", "..")

        assert "255, 105, 114" in email_parent.value_of_css_property("border-color")
        assert "255, 105, 114" in password_parent.value_of_css_property("border-color")
        assert "255, 105, 114" in confirm_password_parent.value_of_css_property("border-color")

class TestRegistrationExistingEmail:

    def test_registration_existing_email(self, driver):
        driver.find_element(*LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.element_to_be_clickable(NO_ACCOUNT_BUTTON)
        ).click()

        driver.find_element(*EMAIL_FIELD).send_keys("imkliuchi@mail.com")
        driver.find_element(*PASSWORD_FIELD).send_keys("test1234")
        driver.find_element(*CONFIRM_PASSWORD_FIELD).send_keys("test1234")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        error = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(EMAIL_ERROR))

        assert "Ошибка" in error.text

        email_field = driver.find_element(*EMAIL_FIELD)
        password_field = driver.find_element(*PASSWORD_FIELD)
        confirm_password_field = driver.find_element(*CONFIRM_PASSWORD_FIELD)

        email_parent = email_field.find_element("xpath", "..")
        password_parent = password_field.find_element("xpath", "..")
        confirm_password_parent = confirm_password_field.find_element("xpath", "..")

        assert "255, 105, 114" in email_parent.value_of_css_property("border-color")
        assert "255, 105, 114" in password_parent.value_of_css_property("border-color")
        assert "255, 105, 114" in confirm_password_parent.value_of_css_property("border-color")
