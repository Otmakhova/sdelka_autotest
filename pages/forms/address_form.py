# TODO: сюда вынести заполнение адресного контрола
# Форма адресного контрола была открыта ранее
from pages.base_page import BasePage
from pages.locators import CommonPatternLocators
from pages.locators import AddressFormLocators
from data_test.load_csv import load_test_data

test_data = load_test_data()
ADDRESS = dict(zip(test_data["address_id"], test_data["address_value"]))


class AddressForm(BasePage):
    def should_be_address_form(self):
        assert self.is_element_present(
            *AddressFormLocators.ADDRESS_FORM_TITLE), "Address form is not present"

    def fill_address_form(self):
        self.should_be_address_form()
        self.click_by_id("addr1btnToggleAddrDetails")
        # пока не работает
        # self.select_dropdown("addr1RegionCode_listbox",
        #           "Республика Башкортостан")
        for key, value in ADDRESS.items():
            self.send_key_by_id(key, value)
        self.click_by_locator(AddressFormLocators.ADDRESS_FORM_SUBMIT)

    # def check_address_form_value(self):
