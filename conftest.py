import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.request_page import RequestPage
import subprocess
import time
import allure
import json
from allure_commons.types import AttachmentType


@pytest.fixture(scope="function")
def browser(request, variables):
    global browser
    print("\nstart browser for test..")
    options = Options()
    options.add_extension(variables['cryptoproextension_path'])
    browser = webdriver.Chrome(
        executable_path=variables['webdriver_path'], options=options)
    browser.maximize_window()
    browser.implicitly_wait(20)
    login_user(variables)
    yield browser
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            allure.attach(browser.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=AttachmentType.PNG)
        except:
            print("\nscreenshot failed..")
            pass  # just ignore
    print("\nquit browser..")
    browser.quit()
    return browser


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


def login_user(variables):
    # параметры можно передавать так https://www.reddit.com/r/learnpython/comments/47gbgf/pytest_advice_sharing_a_token_between_tests/
    LOGIN_LINK = variables['enviroment']
    page = LoginPage(
        browser, LOGIN_LINK)
    page.open()
    page.should_be_login_page()
    page.login(variables['login'], variables['password'],
               variables['certificate'])
    request_page = RequestPage(browser, browser.current_url)
    request_page.should_be_request_page()


@pytest.fixture(scope="session", autouse=True)
def generate_test_data():
    with open("data_test/test_data.json", 'r', encoding='utf-8') as File:
        data = json.load(File)
    # генерация представителя юл на основе данных о фл
    data["ul"]["agent"]["FlSubjectFio"] = data["fl"]["subject"]["LastName"] + ' ' + \
        data["fl"]["subject"]["FirstName"] + ' ' + \
        data["fl"]["subject"]["MiddleName"]
    data["ul"]["agent"]["BirthDateStr"] = data["fl"]["subject"]["BirthDate"]
    data["ul"]["agent"]["Snils"] = data["fl"]["subject"]["Snils"]
    data["ul"]["agent"]["Inn"] = data["fl"]["subject"]["Inn"]
    data["ul"]["agent"]["DocInfo"] = data["fl"]["subject"]["DocSeries"] + \
        ' ' + data["fl"]["subject"]["DocNumber"]
    data["ul"]["agent"]["DocDateStr"] = data["fl"]["subject"]["DocDate"]
    data["ul"]["agent"]["DocIssuerOrgan"] = data["fl"]["subject"]["DocIssuerOrgan"]
    data["ul"]["agent"]["DocIssuerCode"] = data["fl"]["subject"]["DocIssuerCode"]
    data["ul"]["agent"]["Phone"] = '7' + data["fl"]["subject"]["Phone"]
    data["ul"]["agent"]["Email"] = data["fl"]["subject"]["Email"]
    # генерация адресной строки, область пока захардкожена
    data["ul"]["agent"]["Address"] = "Оренбургская Область, р-н " + data["common_form"]["address"]["addr1District"] + ", г " + data["common_form"]["address"]["addr1City"] + ", д " + data["common_form"]["address"]["addr1Locality"] + ", ул " + data["common_form"]["address"]["addr1Street"] + \
        ", д " + data["common_form"]["address"]["addr1House"] + ", корп " + data["common_form"]["address"]["addr1Building"] + \
        ", с " + data["common_form"]["address"]["addr1Structure"] + \
        ", кв " + data["common_form"]["address"]["addr1Apartment"]
    with open("data_test/generated_test_data.json", "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)
    print("\nTest data generated")
