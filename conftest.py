import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
    options.add_extension(
        './CryptoPro-Extension-for-CAdES-Browser-Plug-in-Chrome-Web-Mağazası_v1.2.7.crx')
    browser = webdriver.Chrome(
        executable_path='C:/chromedriver/chromedriver.exe', options=options)
    browser.implicitly_wait(20)
    yield browser
    print("\nquit browser..")
    browser.quit()
