# Форма адресного контрола была открыта ранее
from pages.base_page import BasePage
from pages.locators import CommonPatternLocators
from pages.locators import AddressFormLocators
from data_test.load_test_data import load_test_data_json

ADDRESS = load_test_data_json("common_form", "address")
# TODO: Разобраться с регионом
ADDRESS_STR = "Оренбургская Область, р-н " + ADDRESS.get("addr1District") + ", г " + ADDRESS.get("addr1City") + ", д " + ADDRESS.get("addr1Locality") + ", ул " + ADDRESS.get(
    "addr1Street") + ", д " + ADDRESS.get("addr1House") + ", корп " + ADDRESS.get("addr1Building") + ", с " + ADDRESS.get("addr1Structure") + ", кв " + ADDRESS.get("addr1Apartment")


class AddressForm(BasePage):
    def should_be_address_form(self):
        assert self.is_element_present(
            *AddressFormLocators.ADDRESS_FORM_TITLE), "Address form is not present"

    def fill_address_form(self):
        self.should_be_address_form()
        self.click_by_locator(AddressFormLocators.ADDRESS_FORM_UNCOLLAPSE)
        # пока не работает
        # self.select_dropdown("addr1RegionCode_listbox",
        #           "Республика Башкортостан")
        for key, value in ADDRESS.items():
            self.send_key_by_id(key, value)
        self.click_by_locator(AddressFormLocators.ADDRESS_FORM_SUBMIT)

    def check_address_form_value(self):
        self.check_text_by_id("AddressStr", ADDRESS_STR)
