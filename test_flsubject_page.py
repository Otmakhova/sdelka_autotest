from pages.flsubject_page import FlsubjectPage
from data_test.load_test_data import load_test_data_json
import pytest


@pytest.mark.run(order=1)
@pytest.mark.parametrize("fl_type", ["subject", "subject_for_developer", "subject_for_bank", "subject_for_ul"])
def test_create_flsubject(browser, fl_type):
    FLSUBJECT_DATA = load_test_data_json("fl", fl_type)
    page = FlsubjectPage(
        browser, browser.current_url)
    page.go_to_flsubject_menu()
    page.create_flsubject(FLSUBJECT_DATA)
# TODO: редактирование ФЛ, выпуск серта, фильтрация реестра'''


def test_get_fl_certificate(browser):
    FLSUBJECT_DATA = load_test_data_json("fl", "subject")
    page = FlsubjectPage(
        browser, browser.current_url)
    page.go_to_flsubject_menu()
    page.get_certificate(FLSUBJECT_DATA)
