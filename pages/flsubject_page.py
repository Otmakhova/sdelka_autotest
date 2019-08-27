from .base_page import BasePage
from .locators import CommonPatternLocators
from .locators import FlsubjectPageLocators

ID = ["LastName", "FirstName", "MiddleName", "Snils", "Inn", "BirthDate", "BirthPlace",
      "DocSeries", "DocNumber", "DocIssuerOrgan", "DocIssuerCode", "DocDate", "Phone", "Email"]
VALUE = ["Автотестов", "Автотест", "Автотестович",
         "00373382118", "526317984689", "01.07.1980", "г. Оренбург", "5316", "571230", "УФМС России по Оренбургской области", "560-001", "15.07.2013", "9292222323", "test@amail.ru"]
ADDRESS_ID = ["addr1Okato", "addr1Oktmo", "addr1PostalCode", "addr1District", "addr1City",
              "addr1Locality", "addr1Street", "addr1House", "addr1Building", "addr1Structure", "addr1Apartment"]
ADDRESS_VALUE = ["45272576000", "45331000", "123456", "Северный",
                 "Зеленоград", "Менделеево", "Новая", "909", "1", "1", "47"]
ADDRESS_STR = "Республика Бурятия, р-н Северный, г Зеленоград, д Менделеево, ул Новая, д 909, корп 1, с 1, кв 47"
INPUT_DATA = dict(zip(ID, VALUE))
ADDRESS = dict(zip(ADDRESS_ID, ADDRESS_VALUE))


class FlsubjectPage(BasePage):
    def should_be_flsubject_page(self):
        self.should_be_flsubject_grid()
        self.should_be_flsubject_url()
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

    def should_be_address_form(self):
        assert self.is_element_present(
            *FlsubjectPageLocators.FLSUBJECT_ADRESS_FORM_TITLE), "Flsubject adress from is not present"

    def create_flsubject(self):
        self.click_by_id("createFlButton")
        # Заполнение основной формы
        for key, value in INPUT_DATA.items():
            self.send_key_by_id(key, value)
        self.select_dropdown("SexId_listbox", "Женский")
        # Заполнение формы адреса
        self.click_by_id("link_open_address_modal")
        self.should_be_address_form()
        self.click_by_id("addr1btnToggleAddrDetails")
        for key, value in ADDRESS.items():
            self.send_key_by_id(key, value)
        self.click_by_locator(
            FlsubjectPageLocators.FLSUBJECT_ADRESS_FORM_SUBMIT)
        # Сохранение всей формы, бывает проблема, нужно наблюдать
        self.click_by_locator(
            CommonPatternLocators.get_btn_locator(self, "Сохранить"))
        # Проверка успешного сохранения формы
        self.should_be_flsubject_edit_page(INPUT_DATA)

    def go_to_flsubject_menu(self):
        self.browser.find_element(
            *CommonPatternLocators.get_menu_link_locator(self, "/FlSubject")).click()
        self.should_be_flsubject_page()
