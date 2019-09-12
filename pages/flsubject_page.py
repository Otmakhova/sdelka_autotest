from .base_page import BasePage
from .forms.address_form import AddressForm
from .locators import CommonPatternLocators
from .locators import FlsubjectPageLocators
from data_test.load_csv import load_test_data
from selenium.webdriver.support.ui import WebDriverWait


test_data = load_test_data("flsubject_data.csv")
INPUT_DATA = dict(zip(test_data["flsubject_id"], test_data["flsubject_value"]))


class FlsubjectPage(BasePage):
    def should_be_flsubject_page(self):
        self.should_be_flsubject_grid()
        self.should_be_flsubject_url()
        # Заголовок
        # TODO: Проверить все параметры главной страницы

    def should_be_flsubject_edit_page(self, edit_data):
        self.should_be_flsubject_edit_url()
        self.should_be_flsubject_edit_form(edit_data)
        self.should_be_flsubject_certificate_form()

    def should_be_flsubject_certificate_form(self):
        assert self.is_element_present(
            *FlsubjectPageLocators.FLSUBJECT_CERTIFICATE_INFO), "Flsubject certificate info is not present"

    def should_be_flsubject_edit_url(self):
        assert "FlSubject/Edit" in str(
            self.browser.current_url), "'FlSubject/Edit' is not in current url"

    def should_be_flsubject_edit_form(self, edit_data):
        for key, value in edit_data.items():
            self.check_value_by_id(key, value)

    def should_be_flsubject_url(self):
        assert "FlSubject" in str(
            self.browser.current_url), "'FlSubject' is not in current url"

    def should_be_flsubject_grid(self):
        assert self.is_element_present(
            *FlsubjectPageLocators.FLSUBJECT_GRID), "Flsubject grid is not present"

    def create_flsubject(self):
        self.click_by_id("createFlButton")
        self.check_header_text("h2", "Создание физического лица")
        # Заполнение основной формы
        for key, value in INPUT_DATA.items():
            self.send_key_by_id(key, value)
        self.select_dropdown("SexId_listbox", "Женский")
        # Заполнение формы адреса
        self.click_by_id("link_open_address_modal")
        address_form = AddressForm(self.browser, self.browser.current_url)
        address_form.fill_address_form()
        # Сохранение всей формы, бывает проблема, нужно наблюдать
        self.click_by_locator(
            CommonPatternLocators.get_btn_locator(self, "Сохранить"))
        # Проверка успешного сохранения формы
        self.should_be_flsubject_edit_page(INPUT_DATA)
        address_form.check_address_form_value()
        self.go_to_flsubject_menu()
        self.should_be_registry_element(INPUT_DATA.get(
            "LastName") + " " + INPUT_DATA.get("FirstName") + " " + INPUT_DATA.get("MiddleName"))

    # Можно заменить на базовый метод
    def go_to_flsubject_menu(self):
        self.click_by_link("/FlSubject")
        self.should_be_flsubject_page()
