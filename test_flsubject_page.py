from pages.login_page import LoginPage
from pages.flsubject_page import FlsubjectPage
import pytest


def test_create_flsubject(browser):
    page = FlsubjectPage(
        browser, browser.current_url)
    page.go_to_flsubject_menu()
    page.create_flsubject()