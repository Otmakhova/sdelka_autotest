from .base_page import BasePage
from .forms.address_form import AddressForm
from .flsubject_page import FlsubjectPage
from .locators import CommonPatternLocators
from .locators import UlsubjectPageLocators
from data_test.load_csv import load_test_data
# TODO: вынести все данные в начало
# test_data = load_test_data("ulsubject_data.csv")
# NPUT_DATA = dict(zip(test_data["ulsubject_id"], test_data["ulsubject_value"]))
flsubject_data = load_test_data("flsubject_data.csv")
ulsubject_data = load_test_data("ulsubject_data.csv")
FLSUBJECT_DATA = dict(
    zip(flsubject_data["flsubject_id"], flsubject_data["flsubject_value"]))


class UlsubjectPage(BasePage):
    def should_be_ulsubject_page(self):
        self.should_be_ulsubject_grid()
        self.should_be_ulsubject_url()
        self.check_header_text("h3", "Юридические лица")

    def should_be_ulsubject_edit_page(self, edit_data):
        self.should_be_ulsubject_edit_url()
        self.should_be_ulsubject_edit_form(edit_data)
        self.should_be_ulsubject_agent_form()
        self.check_header_text("h2", "Редактирование юридического лица")

    def should_be_ulsubject_agent_form(self):
        assert self.is_element_present(
            *UlsubjectPageLocators.ULSUBJECT_AGENT_GRID), "Ulsubject Agent form info is not present"

    def should_be_ulsubject_edit_form(self, edit_data):
        for key, value in edit_data.items():
            self.check_value_by_id(key, value)

    def should_be_ulsubject_edit_url(self):
        assert "UlSubject/Edit" in str(
            self.browser.current_url), "'UlSubject/Edit' is not in current url"

    def should_be_ulsubject_url(self):
        assert "UlSubject" in str(
            self.browser.current_url), "'UlSubject' is not in current url"

    def should_be_ulsubject_grid(self):
        assert self.is_element_present(
            *UlsubjectPageLocators.ULSUBJECT_GRID), "Ulsubject grid is not present"

    def check_agent_flsubject_info(self):
        agent_info = [FLSUBJECT_DATA.get("LastName") + ' ' + FLSUBJECT_DATA.get("FirstName") + ' ' + FLSUBJECT_DATA.get(
            "MiddleName"), FLSUBJECT_DATA.get("BirthDate"), FLSUBJECT_DATA.get("Snils"), FLSUBJECT_DATA.get(
            "Inn"), FLSUBJECT_DATA.get("DocSeries") + ' ' + FLSUBJECT_DATA.get("DocNumber"), FLSUBJECT_DATA.get(
            "DocDate"), FLSUBJECT_DATA.get("DocIssuerOrgan"), FLSUBJECT_DATA.get("DocIssuerCode"), '7' + FLSUBJECT_DATA.get(
            "Phone"), FLSUBJECT_DATA.get("Email")]
        AGENT_DATA = dict(zip(ulsubject_data["agent_info_id"], agent_info))
        self.should_be_info_form(AGENT_DATA, 'agent_fl_subject_info') # сомнительная реализация

    def create_ulagent(self, name, ul_type):
        self.click_by_locator(
            UlsubjectPageLocators.get_ulsubject_registry_locator_by_name_and_type(self, name, ul_type))
        self.check_header_text("h2", "Редактирование юридического лица")
        self.should_be_ulsubject_edit_url()
        self.click_by_locator(UlsubjectPageLocators.ULSUBJECT_ADD_AGENT_HREF)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.check_header_text("h2", "Представитель юридического лица")
        agent = FLSUBJECT_DATA.get("LastName") + ' ' + FLSUBJECT_DATA.get("FirstName") + ' ' + FLSUBJECT_DATA.get(
            "MiddleName") + ', СНИЛС: ' + FLSUBJECT_DATA.get("Snils")
        self.select_dropdown('FlSubjectId_listbox',  agent)
        self.click_by_id('btn_save_form')
        self.check_agent_flsubject_info()

    def create_ulsubject(self, ul_type):
        test_data = load_test_data("ulsubject_data.csv")
        INPUT_DATA = dict(
            zip(test_data["ulsubject_id"], test_data["ulsubject_value"]))

        self.click_by_id("createUlButton")
        ul_name = INPUT_DATA.pop("Name") + ul_type
        self.send_key_by_id("Name", ul_name)
        # Заполнение основной формы
        for key, value in INPUT_DATA.items():
            self.send_key_by_id(key, value)
        self.select_dropdown("UlTypeId_listbox", ul_type)
        # Заполнение формы адреса
        self.click_by_id("link_open_address_modal")
        address_form = AddressForm(self.browser, self.browser.current_url)
        address_form.fill_address_form()
        # Сохранение всей формы, бывает проблема, нужно наблюдать
        self.click_by_locator(
            CommonPatternLocators.get_btn_locator(self, "Сохранить"))
        # Проверка успешного сохранения формы
        self.should_be_ulsubject_edit_page(INPUT_DATA)
        address_form.check_address_form_value()
        self.go_to_ulsubject_menu()
        self.should_be_registry_element(ul_name)

    def go_to_ulsubject_menu(self):
        self.click_by_link("/UlSubject")
        self.should_be_ulsubject_page()
