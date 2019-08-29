from .base_page import BasePage
from .locators import CommonPatternLocators
from .locators import UlsubjectPageLocators


class UlsubjectPage(BasePage):
    # def should_be_ulsubject_page(self):
    def create_ulsubject(self):
        self.click_by_id("createUlButton")
