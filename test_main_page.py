from pages.login_page import LoginPage
from pages.request_page import RequestPage
import pytest


def test_page_after_register(browser):
    request_page = RequestPage(browser, browser.current_url)
    request_page.should_be_request_page()
    # TODO: Проверить пункты меню (в зависимости от роли?)
