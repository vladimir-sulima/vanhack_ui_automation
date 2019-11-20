from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from VanHack_WebApp.tests.conftest import *


class WebDriverWrapper:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, config_wait_time)

    def wait_find_and_click(self, locator):
        self.wait.until(ec.presence_of_element_located(locator))
        self.browser.find_element(*locator).click()

    def find_and_click(self, locator, how=None):
        if how is None:
            self.browser.find_element(*locator).click()
        else:
            self.browser.find_element(how, locator).click()

    def find_and_set_text(self, locator, text, how=None):
        if how is None:
            element = self.browser.find_element(*locator)
        else:
            element = self.browser.find_element(how, locator)

        element.clear()
        element.send_keys(text)

    def find_and_select_ddl_option_by_text(self, locator, option_name):
        select = Select(self.browser.find_element(*locator))
        select.select_by_visible_text(option_name)

        return self

    def find_and_get_text(self, locator, how=None):
        if how is None:
            element = self.browser.find_element(*locator)
        else:
            element = self.browser.find_element(how, locator)

        return element.text

    def find_element(self, locator, how=None):
        if how is None:
            element = self.browser.find_element(*locator)
        else:
            element = self.browser.find_element(how, locator)

        return element

    def find_all_elements(self, locator, how=None):
        if how is None:
            elements = self.browser.find_elements(*locator)
        else:
            elements = self.browser.find_elements(how, locator)

        return elements

    def check_element_displayed(self, locator, how=None):
        if how is None:
            element = self.browser.find_element(*locator)
        else:
            element = self.browser.find_element(how, locator)

        return  element.is_displayed()