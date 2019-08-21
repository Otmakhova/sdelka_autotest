from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import CommonPatternLocators


class BasePage(object):
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        return self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def should_be_logout_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def send_key_by_locator(self, locator, key):
        self.browser.find_element(*locator).send_keys(key)

    def click_by_locator(self, locator):
        self.browser.find_element(*locator).click()

    # dropdown не имеют label, элементы спрятаны в span и не отображаются, поэтому нужно искать по aria_owns
    def select_dropdown(self, aria_owns, dropdown_text):
        self.browser.find_element(
            *CommonPatternLocators.get_dropdown_locator_by_aria_owns(self, aria_owns)).click()
        self.browser.find_element(
            *CommonPatternLocators.get_dropdown_value_locator_by_li_text(self, dropdown_text)).click()
