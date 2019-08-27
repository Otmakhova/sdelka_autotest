from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
from .locators import CommonPatternLocators

# TODO: проверка наличия меню
# Пример javascript $('#RegActionIdCombobox').data('kendoDropDownList').dataSource.data() $('#RegActionIdCombobox').data('kendoDropDownList').value(6)


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

    def send_key_by_id(self, id, key):
        self.send_key_by_locator(
            CommonPatternLocators.get_input_locator_by_id(self, id), key)

    def click_by_locator(self, locator):
        self.browser.find_element(*locator).click()

    def click_by_id(self, id):
        self.click_by_locator(
            CommonPatternLocators.get_element_by_id(self, id))

    # dropdown не имеют label, элементы спрятаны в span и не отображаются, поэтому нужно искать по aria_owns
    def select_dropdown(self, aria_owns, dropdown_text):
        self.browser.find_element(
            *CommonPatternLocators.get_dropdown_locator_by_aria_owns(self, aria_owns)).click()
        self.browser.find_element(
            *CommonPatternLocators.get_dropdown_value_locator_by_li_text(self, dropdown_text)).click()

    def check_value_by_id(self, id, value):
        assert self.browser.find_element(
            *CommonPatternLocators.get_element_by_id(self, id)).get_attribute("value") == value, "Element with ID = " + id + " and value = " + value + " is not present"

    def check_text_by_id(self, id, text):
        assert self.browser.find_element(
            *CommonPatternLocators.get_element_by_id(self, id)).text == text, "Element with ID = " + id + " and text = " + text + " is not present"
