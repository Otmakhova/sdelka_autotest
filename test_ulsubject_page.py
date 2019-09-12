from pages.ulsubject_page import UlsubjectPage
import pytest


def test_create_ulsubject(browser):
    page = UlsubjectPage(
        browser, browser.current_url)
    page.go_to_ulsubject_menu()
    page.create_ulsubject("Юридическое лицо")
# TODO: редактирование ЮЛ, выпуск серта, фильтрация реестра


def test_create_developer_ulsubject(browser):
    page = UlsubjectPage(
        browser, browser.current_url)
    page.go_to_ulsubject_menu()
    page.create_ulsubject("Застройщик")


def test_create_bank_ulsubject(browser):
    page = UlsubjectPage(
        browser, browser.current_url)
    page.go_to_ulsubject_menu()
    page.create_ulsubject("Банк")
