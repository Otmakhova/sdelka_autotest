from .base_page import BasePage
from .locators import CommonPatternLocators
from .locators import FlsubjectPageLocators

INPUT_LIST = ["Фамилия", "Имя", "Отчество",
              "СНИЛС", "ИНН", "Дата рождения", "Место рождения", "Кем выдан", "Подразделение", "Дата выдачи", "Телефон", "Email"]

INPUT_KEYS = ["Автотестов", "Автотест", "Автотестович",
              "00373382118", "526317984689", "01.07.1980", "г. Оренбург", "УФМС России по Оренбургской области", "560-001", "15.07.2013", "9292222323", "test@amail.ru"]


class FlsubjectPage(BasePage):
    def should_be_flsubject_page(self):
        self.should_be_flsubject_grid()
        self.should_be_flsubject_url()
        # TODO: Проверить все параметры главной страницы

    def should_be_flsubject_url(self):
        # реализуйте проверку на корректный url адрес
        assert "FlSubject" in str(
            self.browser.current_url), "'FlSubject' is not in current url"

    def should_be_flsubject_grid(self):
        assert self.is_element_present(
            *FlsubjectPageLocators.FLSUBJECT_GRID), "Flsubject grid is not present"

    def should_be_address_form(self):
        assert self.is_element_present(
            *FlsubjectPageLocators.FLSUBJECT_ADRESS_FORM_TITLE), "Flsubject adress from is not present"

    def create_flsubject(self):
        input_dict = dict(zip(INPUT_LIST, INPUT_KEYS))
        self.click_by_locator(
            CommonPatternLocators.get_btn_locator(self, "Создать"))
        # Возможно вынести заполнение в отдельную функцию
        for key, value in input_dict.items():
            self.send_key_by_locator(
                CommonPatternLocators.get_input_locator_by_label(self, key), value)
        self.send_key_by_locator(
            CommonPatternLocators.get_input_locator_by_id(self, "DocSeries"), "5316")
        self.send_key_by_locator(
            CommonPatternLocators.get_input_locator_by_id(self, "DocNumber"), "571230")
        # TODO: Смена пола $('#RegActionIdCombobox').data('kendoDropDownList').dataSource.data() $('#RegActionIdCombobox').data('kendoDropDownList').value(6)
        self.select_dropdown("SexId_listbox", "Женский")
        self.click_by_locator(CommonPatternLocators.get_element_by_id(
            self, "link_open_address_modal"))
        self.should_be_address_form()
        self.click_by_locator(CommonPatternLocators.get_element_by_id(self,
                                                                      "addr1btnToggleAddrDetails"))
        self.send_key_by_locator(
            CommonPatternLocators.get_element_by_id(self, "addr1Okato"), "45272576000")
        self.send_key_by_locator(
            CommonPatternLocators.get_element_by_id(self, "addr1PostalCode"), "124575")
        # TODO: Полное заполнение формы адреса
        self.click_by_locator(
            FlsubjectPageLocators.FLSUBJECT_ADRESS_FORM_SUBMIT)
        self.click_by_locator(
            CommonPatternLocators.get_element_by_id(self, "btn_save_form"))
        self.should_be_flsubject_page()

    def go_to_flsubject_menu(self):
        self.browser.find_element(
            *CommonPatternLocators.get_menu_link_locator(self, "/FlSubject")).click()
        self.should_be_flsubject_page()
