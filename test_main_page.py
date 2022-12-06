import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # link_login = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    
    page = MainPage(browser, link)
    page.open()

    time.sleep(2)
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

    time.sleep(2)
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_see_basket_clear()
