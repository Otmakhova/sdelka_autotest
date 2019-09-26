from pages.ulsubject_page import UlsubjectPage
from data_test.load_test_data import load_test_data_json
import pytest

@pytest.mark.run(order=2)
@pytest.mark.parametrize("ul_type", ["Юридическое лицо", "Застройщик", "Банк"])
def test_create_ulsubject(browser, ul_type):
    ULSUBJECT_DATA = load_test_data_json("ul", "subject")
    page = UlsubjectPage(
        browser, browser.current_url)
    page.go_to_ulsubject_menu()
    page.create_ulsubject(ULSUBJECT_DATA, ul_type)
# TODO: редактирование ЮЛ, выпуск серта, фильтрация реестра

@pytest.mark.run(order=3)
@pytest.mark.parametrize("ulagent_type,ul_name,ul_type", [("agent", "ООО Тестовый Юридическое лицо", "Юридическое лицо"), ("agent_developer", "ООО Тестовый Застройщик", "Застройщик"), ("agent_bank", "ООО Тестовый Банк", "Банк")])
def test_create_ulagent(browser, ulagent_type, ul_name, ul_type):
    ULAGENT_DATA = load_test_data_json("ul", ulagent_type)
    page = UlsubjectPage(browser, browser.current_url)
    page.go_to_ulsubject_menu()  # Можно вынести в фикстуру класса?
    page.create_ulagent(ULAGENT_DATA, ul_name, ul_type)
