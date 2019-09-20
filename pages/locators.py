from typing import Tuple
from selenium.webdriver.common.by import By


class CommonPatternLocators(object):
    def get_placeholder_locator(self, placeholder_name):  # возможно не нужен
        placeholder_link = (
            By.XPATH, ".//input[@placeholder='" + str(placeholder_name) + "']")
        return placeholder_link

    def get_btn_locator(self, btn_name):
        btn_link = (By.XPATH, ".//button[text()='" + str(btn_name) + "']")
        return btn_link

    def get_input_locator_by_id(self, input_id):
        input_link = (By.XPATH, ".//input[@id='" + str(input_id) + "']")
        return input_link

    def get_input_locator_by_label(self, label_name):
        input_link = (
            # хулиганство, которое работает, но лучше так не делать
            # для того, чтобы обрабатывать два инпута на одной строке
            By.XPATH, ".//label[text()= '" + str(label_name) + "']/following-sibling::div//input[1]")
        return input_link

    def get_link_locator(self, menu_link):
        link = (By.XPATH, ".//a[@href='" + str(menu_link) + "']")
        return link

    def get_dropdown_locator_by_aria_owns(self, aria_owns):
        dropdown = (By.CSS_SELECTOR, "[aria-owns='" + aria_owns + "']")
        return dropdown

    def get_dropdown_value_locator_by_li_text(self, text):
        dropdown_value = (By.XPATH, ".//li[text()='" + text + "']")
        return dropdown_value

    def get_element_by_id(self, id, parent=None):
        if parent is None:
            element = (By.CSS_SELECTOR, "#" + id)
        else:
            element = (By.CSS_SELECTOR, "#" + parent + ' '+ "#" + id)
        return element

    def get_registry_element_locator(self, registry_element):
        registry_element_locator = (
            By.XPATH, "//table//b[contains(text(), '" + registry_element + "')]")
        return registry_element_locator

    def get_header_locator(self, level):
        header_locator = (By.CSS_SELECTOR, str(level))
        return header_locator


class BasePageLocators(object):
    LOGOUT_LINK = (By.XPATH, ".//a[@href='/Account/LogOut']")
    USER_ICON = (By.CSS_SELECTOR, "#pic")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    def get_login_certificate(self, cert_name):
        login_cert_link = (By.XPATH, "//span[text()='" + str(cert_name) + "']")
        return login_cert_link


class RequestPageLocators(object):
    REQUEST_GRID = (By.CSS_SELECTOR, "#gridRequests")


class FlsubjectPageLocators(object):
    FLSUBJECT_GRID = (By.CSS_SELECTOR, "#gridFlSubject")
    FLSUBJECT_CERTIFICATE_INFO = (By.CSS_SELECTOR, ".certificate-info")
    # TODO: Описать параметры главной страницы


class UlsubjectPageLocators(object):
    ULSUBJECT_GRID = (By.CSS_SELECTOR, "#gridUlSubject")
    ULSUBJECT_AGENT_GRID = (By.CSS_SELECTOR, "#ulAgentGrid")
    ULSUBJECT_ADD_AGENT_HREF=(By.XPATH, "//a[contains(text(), 'Добавить представителя')]")

    def get_ulsubject_registry_locator_by_name_and_type(self, name, ul_type):
        registry_element = (
            By.XPATH, "//tr[td[contains(text(),'" + ul_type + "')] and td/b[contains(text(),'" + name + "')]]/td[1]")
        return registry_element


class AddressFormLocators(object):
    ADDRESS_FORM_TITLE = (By.XPATH, ".//span[text()='Ввод адреса']")
    ADDRESS_FORM_SUBMIT = (By.CSS_SELECTOR, "input[value='Сохранить']")
    ADDRESS_FORM_UNCOLLAPSE = (
        By.CSS_SELECTOR, "#addr1btnToggleAddrDetails > i")


class ComplexPageLocators(object):
    COMPLEX_ADDRESS_FORM = (
        By.CSS_SELECTOR, "a[onclick='openAddressControl()']")
    COMPLEX_DEVELOPER_DROPDOWN = (
        By.CSS_SELECTOR, "[aria-controls='DeveloperIdComboBox_listbox']")
    COMPLEX_DIALOG_SUCCESS = (
        By.CSS_SELECTOR, "#dialogWin")
    COMPLEX_GRID = (By.CSS_SELECTOR, "#gridComplex")
    COMPLEX_REGISTER_FROM_CONFIRMATION = (
        By.CSS_SELECTOR, ".confirmation a[href='/Complex']")
