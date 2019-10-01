from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from pages.locators import CommonPatternLocators
from pages.locators import CertificateFormLocators
import allure
import time


class CertificateForm(BasePage):
    @allure.step("Проверка формы сертификата")
    def should_be_certificate_form(self, status):
        self.should_be_certificate_info()
        self.check_header_text(
            "h4", "Информация о сертификате", ".certificate-header")
        self.check_certificate_status(status)

    @allure.step("Проверка наличия окна сертификата")
    def should_be_certificate_info(self):
        assert self.is_element_present(
            *CertificateFormLocators.CERTIFICATE_INFO), "Certificate info is not present"

    @allure.step("Проверка раздела проверки в СМЭВ-3")
    def should_be_smev_check(self):
        self.check_header_text("h2", "Статус проверки в СМЭВ-3", ".smev-check")
        self.is_element_present(
            *CertificateFormLocators.CERTIFICATE_SMEV_CHECK_INN)
        self.is_element_present(
            *CertificateFormLocators.CERTIFICATE_SMEV_CHECK_SNILS)

    @allure.step("Проверка заявления на сертификат")
    def should_be_statment_pdf(self):
        self.check_header_text("h2", "Заявление", ".link-file")
        # TODO: проверить загрузку файла и его наличие

    @allure.step("Проверка окна подтверждения выпуска сертификата")
    def should_be_confirm_dialog(self):
        self.is_element_present(
            *CertificateFormLocators.CERTIFICATE_CONFIRM_TITLE)
        # TODO: проверить остальны элементы

    # TODO: def should_be_display_uploaded_files(self):

    @allure.step("Проверка текущего статуса сертификата")
    def check_certificate_status(self, status):
        is_present = self.is_element_present(
            *CertificateFormLocators.CERTIFICATE_STATUS, timeout=30)
        if (is_present):
            current_status = self.browser.find_element(
                *CertificateFormLocators.CERTIFICATE_STATUS)
            assert current_status.text == status, "Certificate status is not " + \
                status + " current status is " + current_status.text
        else:
            assert is_present == True, "Certificate status did not change yet"

    @allure.step("Выпуск сертификата")
    def issue_certificate(self):
        self.click_by_id("btn_issue_certificate")
        self.check_certificate_status("Проверка данных")
        self.should_be_smev_check()
        self.should_be_statment_pdf()

    @allure.step("Обновление сертификата")
    def update_certificate(self):
        self.click_by_id("btn_update_certificate")
        self.should_be_confirm_dialog()
        self.click_by_id("btn_modal_confirm")
        self.check_certificate_status("Выпущен. Неактивирован")

    @allure.step("Отправка документов в УЦ")
    def upload_documents(self):
        self.upload_pdf_document("Statement")
        self.upload_pdf_document("KeyInfo")
        self.click_by_id("btn_upload_uc_certificate")
        self.check_certificate_status("Выпущен. Активирован")
