from typing import Tuple
from selenium.webdriver.common.by import By


class CommonPatternLocators(object):
    def get_placeholder_locator(self, placeholder_name):
        placeholder_link = (
            By.XPATH, ".//input[@placeholder='" + str(placeholder_name) + "']")
        return placeholder_link

    def get_btn_locator(self, btn_name):
        btn_link = (By.XPATH, ".//button[text()='" + str(btn_name) + "']")
        return btn_link


class BasePageLocators(object):
    LOGOUT_LINK = (By.XPATH, ".//a[@href='/Account/LogOut']")
    USER_ICON = (By.CSS_SELECTOR, "#pic")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_CERTIFICATE = (By.XPATH, '//span[text()="Ульяна"]')


class RequestPageLocators(object):
    REQUEST_GRID = (By.CSS_SELECTOR, "#gridRequests")
