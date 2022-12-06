from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    EMAIL = (By.CSS_SELECTOR, 'input[name="registration-email"]')
    PASSWORD1 = (By.CSS_SELECTOR, 'input[name="registration-password1"]')
    PASSWORD2 = (By.CSS_SELECTOR, 'input[name="registration-password2"]')
    BUTTON_REGISTER = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    FORM_LOGIN = (By.CSS_SELECTOR, 'form#login_form')
    FORM_REGISTER = (By.CSS_SELECTOR, 'form#register_form')

class ProductPageLocators():
    BUTTON_ADD_BASKET = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    TEXT_PRODUCT_SUCCES_ADD = (By.CSS_SELECTOR, 'div.alertinner strong')
    TEXT_PRODUCT = (By.CSS_SELECTOR, 'div.product_main h1')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert-success')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, 'span.btn-group a')
    TEXT_BASKET_CLEAR = (By.CSS_SELECTOR, 'div#content_inner p')