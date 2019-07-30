from pages.login_page import LoginPage
from pages.request_page import RequestPage
import pytest

LOGIN_LINK = "http://10.180.65.15/Account/Logon?ReturnUrl=%2F"


def test_login_user(browser):
    page = LoginPage(
        browser, LOGIN_LINK)
    page.open()
    page.should_be_login_page()
    page.login()
    request_page = RequestPage(browser, browser.current_url)
    request_page.should_be_request_page()
