import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    link_login = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    # page = MainPage(browser, link)
    # page.open()
    # page.go_to_login_page()
    # page.should_be_login_link()

    login_page = LoginPage(browser, link_login)
    login_page.open()
    login_page.should_be_login_url()
    login_page.should_be_login_form()
    login_page.should_be_register_form()

    time.sleep(2)
    