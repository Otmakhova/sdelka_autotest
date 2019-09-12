from pages.complex_page import ComplexPage
import pytest


def test_create_complex(browser):
    page = ComplexPage(
        browser, browser.current_url)
    page.go_to_complex_menu()
    page.create_complex()
# TODO: редактирование комплекса, фильтрация реестра, добавление домов
