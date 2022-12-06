from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_be_see_basket_clear(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_CLEAR), 'Basket is not clear'

    def should_be_not_see_basket_clear(self):
        assert self.is_not_element_present(*BasketPageLocators.TEXT_BASKET_CLEAR), 'Basket is clear'