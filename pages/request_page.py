from .base_page import BasePage
from .locators import CommonPatternLocators
from .locators import RequestPageLocators


class RequestPage(BasePage):
    def should_be_request_page(self):
        self.should_be_request_grid()
        self.should_be_request_url()

    def should_be_request_url(self):
        # реализуйте проверку на корректный url адрес
        assert "Request" in str(
            self.browser.current_url), "'Request' is not in current url"

    def should_be_request_grid(self):
        assert self.is_element_present(
            *RequestPageLocators.REQUEST_GRID), "Request grid is not present"
