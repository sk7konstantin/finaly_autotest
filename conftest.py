import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
        help='Choose browser: chrome or firefox')

@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'chrome':
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == 'firefox':
        print('Install Firefox driver')
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
