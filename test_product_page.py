import time
import pytest
from selenium import webdriver
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

@pytest.mark.skip
@pytest.mark.parametrize('link', ['0','1','2','3','4','5','6','7','8','9'])
def test_guest_can_add_product_to_basket(browser, link):
    # product_link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    # product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    product_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}'

    #todo Инициализировали класс
    page = ProductPage(browser, product_link)
    page.open() #todo Открываем страницу
    time.sleep(1)

    page.should_be_button_basket()  #todo Проверяем кнопку добавления в корзину
    page.add_product_in_basket()    #todo Нажимаем на кнопку
    page.read_allert()              #todo Читаем данные с алерт и вставляем ответ
    page.check_text_after_add_to_basket() #todo Проверяем название товара и название товара 
                                            #todot появляющееся после добавления его в корзину


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_basket()
    page.add_product_in_basket()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Сообщение есть'

def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), 'Сообщение есть'

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_button_basket()
    page.add_product_in_basket()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Сообщение есть'