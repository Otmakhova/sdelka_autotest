from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import CommonPatternLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "Logon" in str(
            self.browser.current_url), "'Logon' is not in current url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), "Form to login is not presented"

    def login(self, login, password, certificate):
        # Логин с сертификатом
        self.browser.find_element(
            *CommonPatternLocators.get_placeholder_locator(self, "Введите логин")).send_keys(login)
        self.browser.find_element(
            *CommonPatternLocators.get_placeholder_locator(self, "Введите пароль")).send_keys(password)
        self.browser.find_element(
            *CommonPatternLocators.get_btn_locator(self, "Войти")).click()
        self.browser.find_element(
            *LoginPageLocators.get_login_certificate(self, certificate)).click()

# TODO: Логин без сертификата
