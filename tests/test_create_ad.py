import random
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import (
    PLACE_AD_BUTTON,
    LOGIN_REQUIRED_MESSAGE,
    NEW_AD_TITLE,
    AD_NAME_FIELD,
    AD_DESCRIPTION_FIELD,
    AD_PRICE_FIELD,
    DROPDOWN_BUTTONS,
    HOBBY_CATEGORY,
    KAZAN_CITY,
    AD_RADIO_BUTTON,
    PUBLISH_BUTTON,
    PROFILE_BUTTON,
    PROFILE_AD_NAMES,
    NEXT_ADS_PAGE
)

class TestCreateAdWithoutAuth:

    def test_create_ad_without_auth(self, driver):
        driver.find_element(*PLACE_AD_BUTTON).click()

        message = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LOGIN_REQUIRED_MESSAGE))

        assert message.text == "Чтобы разместить объявление, авторизуйтесь"

class TestCreateAdWithAuth:

    def test_create_ad_with_auth(self, logged_in_driver):
        wait = WebDriverWait(logged_in_driver, 5)

        logged_in_driver.find_element(*PLACE_AD_BUTTON).click()
        wait.until(expected_conditions.visibility_of_element_located(NEW_AD_TITLE))

        ad_name = f"Коньки{random.randint(10000, 99999)}"
        logged_in_driver.find_element(*AD_NAME_FIELD).send_keys(ad_name)
        logged_in_driver.find_element(*AD_DESCRIPTION_FIELD).send_keys("Продаю коньки женские 38 размера. Цвет белый")
        logged_in_driver.find_element(*AD_PRICE_FIELD).send_keys("1000")
        logged_in_driver.find_elements(*DROPDOWN_BUTTONS)[0].click()
        logged_in_driver.find_element(*HOBBY_CATEGORY).click()
        logged_in_driver.find_elements(*DROPDOWN_BUTTONS)[1].click()
        logged_in_driver.find_element(*KAZAN_CITY).click()
        logged_in_driver.find_element(*AD_RADIO_BUTTON).click()

        logged_in_driver.find_element(*PUBLISH_BUTTON).click()

        wait.until(expected_conditions.url_to_be("https://qa-desk.education-services.ru/"))

        logged_in_driver.execute_script("window.scrollTo(0, 0);")
        wait.until(expected_conditions.presence_of_element_located(PROFILE_BUTTON))
        logged_in_driver.execute_script("document.querySelector('button.circleSmall').click();")

        wait.until(expected_conditions.presence_of_all_elements_located(PROFILE_AD_NAMES))

        next_button = logged_in_driver.find_elements(*NEXT_ADS_PAGE)
        while next_button and next_button[0].is_enabled():
            next_button[0].click()
            wait.until(expected_conditions.presence_of_all_elements_located(PROFILE_AD_NAMES))
            next_button = logged_in_driver.find_elements(*NEXT_ADS_PAGE)

        wait.until(expected_conditions.presence_of_all_elements_located(PROFILE_AD_NAMES))

        ads = logged_in_driver.find_elements(*PROFILE_AD_NAMES)

        assert any(ad.text == ad_name for ad in ads)
