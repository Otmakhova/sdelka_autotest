from pages.complex_page import ComplexPage
from data_test.load_test_data import load_test_data_json
import pytest


@pytest.mark.run(order=4)
def test_create_complex(browser):
    COMPLEX_DATA = load_test_data_json("complex", "subject")
    page = ComplexPage(
        browser, browser.current_url)
    page.go_to_complex_menu()
    page.create_complex(COMPLEX_DATA)
# TODO: редактирование комплекса, фильтрация реестра, добавление домов
