import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException

from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_product_in_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET).click()

    def should_be_button_basket(self):
        assert self.browser.find_element(*ProductPageLocators.BUTTON_ADD_BASKET), 'Not button add in basket'

    def read_allert(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_text_after_add_to_basket(self):
        text_product = self.browser.find_element(*ProductPageLocators.TEXT_PRODUCT).text.strip()
        text_product_after_add =  self.browser.find_element(*ProductPageLocators.TEXT_PRODUCT_SUCCES_ADD).text.strip()
        assert text_product == text_product_after_add, 'Текст продукта и текст продукта после добавления в корзину не совпадает!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.TEXT_PRODUCT_SUCCES_ADD), \
            'Success message is presented, but should not be'
