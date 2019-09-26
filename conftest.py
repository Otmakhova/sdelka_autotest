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
    fl_agent_pair = [["agent", "subject_for_ul"], ["agent_developer",
                                                   "subject_for_developer"], ["agent_bank", "subject_for_bank"]]

    for i in fl_agent_pair:
        data["ul"][i[0]]["FlSubjectFio"] = data["fl"][i[1]]["LastName"] + ' ' + \
            data["fl"][i[1]]["FirstName"] + ' ' + \
            data["fl"][i[1]]["MiddleName"]
        data["ul"][i[0]]["BirthDateStr"] = data["fl"][i[1]]["BirthDate"]
        data["ul"][i[0]]["Snils"] = data["fl"][i[1]]["Snils"]
        data["ul"][i[0]]["Inn"] = data["fl"][i[1]]["Inn"]
        data["ul"][i[0]]["DocInfo"] = data["fl"][i[1]]["DocSeries"] + \
            ' ' + data["fl"][i[1]]["DocNumber"]
        data["ul"][i[0]]["DocDateStr"] = data["fl"][i[1]]["DocDate"]
        data["ul"][i[0]]["DocIssuerOrgan"] = data["fl"][i[1]]["DocIssuerOrgan"]
        data["ul"][i[0]]["DocIssuerCode"] = data["fl"][i[1]]["DocIssuerCode"]
        data["ul"][i[0]]["Phone"] = '7' + data["fl"][i[1]]["Phone"]
        data["ul"][i[0]]["Email"] = data["fl"][i[1]]["Email"]
        # генерация адресной строки, область пока захардкожена
        data["ul"][i[0]]["Address"] = "Оренбургская Область, р-н " + data["common_form"]["address"]["addr1District"] + ", г " + data["common_form"]["address"]["addr1City"] + ", д " + data["common_form"]["address"]["addr1Locality"] + ", ул " + data["common_form"]["address"]["addr1Street"] + \
            ", д " + data["common_form"]["address"]["addr1House"] + ", корп " + data["common_form"]["address"]["addr1Building"] + \
            ", с " + data["common_form"]["address"]["addr1Structure"] + \
            ", кв " + data["common_form"]["address"]["addr1Apartment"]

    with open("data_test/generated_test_data.json", "w", encoding='utf-8') as write_file:
        json.dump(data, write_file, ensure_ascii=False)
    print("\nTest data generated")

# обработка юникода в параметрах теста


def pytest_make_parametrize_id(config, val):
    return repr(val)
