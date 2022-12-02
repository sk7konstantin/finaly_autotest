import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
        help='Choose browser: chrome or firefox')

    parser.addoption('--language', action='store', default=None,
        help='Choose laguage: ru or en')


#todo Проверяем какой браузер выбрал пользователь и инициализируем его
#! Все данные считываем из консоли
def check_browser_name(browser_name, options):
    if browser_name == 'chrome':
        print("\nstart browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        print('Install Firefox driver')
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    return browser


#todo Проверяем какой язык выбрал пользователь и передаем его в опции браузера
#! Все данные считываем из консоли
def check_language_user(user_language, options):
    if user_language == 'ru':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
    elif user_language == 'en':
        options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    else:
        raise pytest.UsageError('--language should be ru or en')
    
    return options

#todo Инициализируем браузер и добавляем в него выбранные опции
@pytest.fixture(scope="class")
def browser(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')

    browser = None
    options = Options()
    options = check_language_user(user_language, options)

    browser = check_browser_name(browser_name, options)

    yield browser
    
    print("\nquit browser..")
    browser.quit()
