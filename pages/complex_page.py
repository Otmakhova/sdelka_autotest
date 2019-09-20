from .base_page import BasePage
from .forms.address_form import AddressForm
from .locators import CommonPatternLocators
from .locators import ComplexPageLocators
from data_test.load_csv import load_test_data
from selenium.webdriver.common.action_chains import ActionChains
import time


test_data = load_test_data("complex_data.csv")
INPUT_DATA = dict(zip(test_data["complex_id"], test_data["complex_value"]))


class ComplexPage(BasePage):
    def should_be_complex_page(self):
        self.should_be_complex_grid()
        self.should_be_complex_url()
        self.check_header_text("h3", "Комплексы")

    # TODO: Использовать в тесте на проверку сохраненных данных (Закрыть уведомление)
    def should_be_complex_edit_page(self, edit_data):
        self.should_be_complex_edit_url()
        self.should_be_complex_edit_form(edit_data)
        self.check_header_text("h2", "Редактирование комплекса")

    def should_be_complex_edit_form(self, edit_data):
        for key, value in edit_data.items():
            self.check_value_by_id(key, value)

    def should_be_complex_edit_url(self):
        assert "Complex/Edit" in str(
            self.browser.current_url), "'Complex/Edit' is not in current url: " + str(self.browser.current_url)

    def should_be_complex_grid(self):
        assert self.is_element_present(
            *ComplexPageLocators.COMPLEX_GRID), "Complex grid is not present"

    def should_be_complex_url(self):
        assert "Complex" in str(
            self.browser.current_url), "'Complex' is not in current url"

    def create_complex(self):
        self.click_by_id("createComplexButton")
        # Заполнение основной формы
        for key, value in INPUT_DATA.items():
            self.send_key_by_id(key, value)
        # стандартный селект не подходит, потому что нажатие фиксируется не по всему полю, а только по стрелочке
        self.click_by_locator(ComplexPageLocators.COMPLEX_DEVELOPER_DROPDOWN)
        dropdown_value_locator = self.browser.find_element(
            *CommonPatternLocators.get_dropdown_value_locator_by_li_text(self, "ООО Тестовый Застройщик"))
        ActionChains(self.browser).move_to_element(
            dropdown_value_locator).click(dropdown_value_locator).perform()
        time.sleep(0.1)
        # Заполнение формы адреса
        self.click_by_locator(ComplexPageLocators.COMPLEX_ADDRESS_FORM)
        address_form = AddressForm(self.browser, self.browser.current_url)
        address_form.fill_address_form()
        # Сохранение всей формы
        self.click_by_locator(
            CommonPatternLocators.get_btn_locator(self, "Сохранить"))
        self.should_be_dialog_success()
        self.click_by_locator(
            CommonPatternLocators.get_btn_locator(self, "Закрыть"))
        self.should_be_complex_edit_form(INPUT_DATA)
        self.go_to_complex_menu()
        self.should_be_registry_element(INPUT_DATA.get("ComplexName"))

    # Можно заменить на базовый метод
    def go_to_complex_menu(self):
        self.click_by_link("/Complex")
        self.should_be_complex_page()

    def should_be_dialog_success(self):
        self.is_element_present(*ComplexPageLocators.COMPLEX_DIALOG_SUCCESS)
        # TODO: Написать еще элементы уведомления
