import pytest
from selenium.webdriver.common.by import By
from VanHack_WebApp.pages.EmployersTab.EmployersPage import EmployersPage
from VanHack_WebApp.pages.CommonElements_Abstract import CommonElements
from framework.WebDriverWrapper import WebDriverWrapper


class EventsPage(WebDriverWrapper, CommonElements):
    ALL_HEADER_TABS = (By.XPATH, "//div[@class='NavigationPrimaryMenu']//ul//a")
