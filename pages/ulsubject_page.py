from .base_page import BasePage
from .forms.address_form import AddressForm
from .flsubject_page import FlsubjectPage
from .locators import CommonPatternLocators
from .locators import UlsubjectPageLocators
from data_test.load_test_data import load_test_data_json

FLSUBJECT_DATA = load_test_data_json("fl", "subject")
ULSUBJECT_DATA = load_test_data_json("ul", "subject")
ULAGENT_DATA = load_test_data_json("ul", "agent")


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

    def create_ulagent(self, name, ul_type):
        self.click_by_locator(
            UlsubjectPageLocators.get_ulsubject_registry_locator_by_name_and_type(self, name, ul_type))
        self.check_header_text("h2", "Редактирование юридического лица")
        self.should_be_ulsubject_edit_url()
        self.click_by_locator(UlsubjectPageLocators.ULSUBJECT_ADD_AGENT_HREF)
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.check_header_text("h2", "Представитель юридического лица")
        agent = ULAGENT_DATA.get("FlSubjectFio") + \
            ', СНИЛС: ' + ULAGENT_DATA.get("Snils")
        self.select_dropdown('FlSubjectId_listbox',  agent)
        self.click_by_id('btn_save_form')
        self.should_be_info_form(ULAGENT_DATA, 'agent_fl_subject_info')

    def create_ulsubject(self, ul_type):
        self.click_by_id("createUlButton")
        ULSUBJECT_DATA["Name"] = ULSUBJECT_DATA["Name"] + ul_type
        # Заполнение основной формы
        for key, value in ULSUBJECT_DATA.items():
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
        self.should_be_ulsubject_edit_page(ULSUBJECT_DATA)
        address_form.check_address_form_value()
        self.go_to_ulsubject_menu()
        self.should_be_registry_element(ULSUBJECT_DATA.get("Name"))

    def go_to_ulsubject_menu(self):
        self.click_by_link("/UlSubject")
        self.should_be_ulsubject_page()
