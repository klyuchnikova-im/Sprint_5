from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import LOGOUT_BUTTON, LOGIN_BUTTON


def test_logout(logged_in_driver):
    WebDriverWait(logged_in_driver, 5).until(expected_conditions.element_to_be_clickable(LOGOUT_BUTTON)).click()

    login_button = WebDriverWait(logged_in_driver, 5).until(expected_conditions.element_to_be_clickable(LOGIN_BUTTON))

    assert login_button.text == "Вход и регистрация"
