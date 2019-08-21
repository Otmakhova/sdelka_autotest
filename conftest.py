import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.request_page import RequestPage


@pytest.fixture(scope="function")
def browser(variables):
    global browser
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
    options.add_extension(
        './CryptoPro-Extension-for-CAdES-Browser-Plug-in-Chrome-Web-Mağazası_v1.2.7.crx')
    browser = webdriver.Chrome(
        executable_path='C:/chromedriver/chromedriver.exe', options=options)
    browser.maximize_window()
    browser.implicitly_wait(20)
    login_user(variables)
    yield browser
    print("\nquit browser..")
    browser.quit()
    return browser


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
