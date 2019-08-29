from .base_page import BasePage
from .forms.address_form import AddressForm
from .locators import CommonPatternLocators
from .locators import FlsubjectPageLocators
from data_test.load_csv import load_test_data

ID = ["LastName", "FirstName", "MiddleName", "Snils", "Inn", "BirthDate", "BirthPlace",
      "DocSeries", "DocNumber", "DocIssuerOrgan", "DocIssuerCode", "DocDate", "Phone", "Email"]
VALUE = ["Автотестов", "Автотест", "Автотестович",
         "00373382118", "526317984689", "01.07.1980", "г. Оренбург", "5316", "571230", "УФМС России по Оренбургской области", "560-001", "15.07.2013", "9292222323", "test@amail.ru"]
# TODO: сформировать из файла
ADDRESS_STR = "Республика Бурятия, р-н Северный, г Зеленоград, д Менделеево, ул Новая, д 909, корп 1, с 1, кв 47"
INPUT_DATA = dict(zip(ID, VALUE))


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
        self.check_text_by_id("AddressStr", ADDRESS_STR)

    def should_be_flsubject_url(self):
        assert "FlSubject" in str(
            self.browser.current_url), "'FlSubject' is not in current url"

    def should_be_flsubject_grid(self):
        assert self.is_element_present(
            *FlsubjectPageLocators.FLSUBJECT_GRID), "Flsubject grid is not present"

    def should_be_registry_element(self, registry_element):
        assert self.is_element_present(*CommonPatternLocators.get_registry_element_locator(
            self, registry_element)), "Registry element " + registry_element + " is not present"

    def create_flsubject(self):
        self.click_by_id("createFlButton")
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
        self.go_to_flsubject_menu()
        self.should_be_registry_element(INPUT_DATA.get(
            "LastName") + " " + INPUT_DATA.get("FirstName") + " " + INPUT_DATA.get("MiddleName"))

    def go_to_flsubject_menu(self):
        self.click_by_link("/FlSubject")
        self.should_be_flsubject_page()
