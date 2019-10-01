from .base_page import BasePage
from .forms.address_form import AddressForm
from .forms.certificate_form import CertificateForm
from .locators import CommonPatternLocators
from .locators import FlsubjectPageLocators
from selenium.webdriver.support.ui import WebDriverWait
import allure


class FlsubjectPage(BasePage):
    @allure.step("Проверка главной страницы ФЛ")
    def should_be_flsubject_page(self):
        self.should_be_flsubject_grid()
        self.should_be_flsubject_url()
        self.check_header_text("h3", "Физические лица")

    @allure.step("Проверка формы редактирования ФЛ")
    def should_be_flsubject_edit_page(self, edit_data, status):
        self.should_be_flsubject_edit_url()
        self.should_be_edit_form(edit_data)
        self.should_be_flsubject_certificate_form(status)
        self.check_header_text("h2", "Редактирование физического лица")

    @allure.step("Проверка формы сертификата ФЛ")
    def should_be_flsubject_certificate_form(self, status):
        certificate_form = CertificateForm(
            self.browser, self.browser.current_url)
        certificate_form.should_be_certificate_form(status)

    @allure.step("Проверка url страницы редактирования ФЛ")
    def should_be_flsubject_edit_url(self):
        assert "FlSubject/Edit" in str(
            self.browser.current_url), "'FlSubject/Edit' is not in current url"

    @allure.step("Проверка url страницы ФЛ")
    def should_be_flsubject_url(self):
        assert "FlSubject" in str(
            self.browser.current_url), "'FlSubject' is not in current url"

    @allure.step("Проверка наличия реестра ФЛ")
    def should_be_flsubject_grid(self):
        assert self.is_element_present(
            *FlsubjectPageLocators.FLSUBJECT_GRID), "Flsubject grid is not present"

    @allure.step("Создание ФЛ")
    def create_flsubject(self, flsubject_data):
        self.click_by_id("createFlButton")
        self.check_header_text("h2", "Создание физического лица")
        # Заполнение основной формы
        for key, value in flsubject_data.items():
            self.send_key_by_id(key, value)
        self.select_dropdown("SexId_listbox", "Женский")
        # Заполнение формы адреса
        self.click_by_id("link_open_address_modal")
        address_form = AddressForm(self.browser, self.browser.current_url)
        address_form.fill_address_form()
        self.click_by_locator(
            CommonPatternLocators.get_btn_locator(self, "Сохранить"))
        # Проверка успешного сохранения формы
        self.should_be_flsubject_edit_page(
            flsubject_data, "Сертификат не запрашивался")
        address_form.check_address_form_value()
        self.go_to_flsubject_menu()
        self.should_be_registry_element(flsubject_data.get(
            "LastName") + " " + flsubject_data.get("FirstName") + " " + flsubject_data.get("MiddleName"))

    @allure.step("Выпуск сертификата для ФЛ")
    def get_certificate_for_flsubject(self, flsubject_data):
        self.click_by_locator(FlsubjectPageLocators.get_flsubject_registry_locator_by_name_and_cert_status(self, flsubject_data.get(
            "LastName") + " " + flsubject_data.get("FirstName") + " " + flsubject_data.get("MiddleName"), "Сертификат не выпускался"))
        self.should_be_flsubject_edit_page(
            flsubject_data, "Сертификат не запрашивался")
        certificate_form = CertificateForm(
            self.browser, self.browser.current_url)
        certificate_form.issue_certificate()
        certificate_form.update_certificate()
        certificate_form.upload_documents()

    @allure.step("Переход на главную страницу ФЛ")
    def go_to_flsubject_menu(self):
        self.click_by_link("/FlSubject")
        self.should_be_flsubject_page()
