from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        sub_string = 'login'
        assert sub_string in self.url, 'Wrong url!'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), 'selector wrong or not form for login'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTER), 'selector wrong or not form for register'

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER).click()