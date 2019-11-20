from abc import ABC
import pytest

from selenium.webdriver.common.by import By

from framework.WebDriverWrapper import WebDriverWrapper


class CommonElements(ABC):

    # region Locators
    ALL_HEADER_TABS = (By.XPATH, "//header//ul//a")
    EMPLOYERS_TAB = (By.XPATH, "//a[text()='Employers']/..")
    TALENT_TAB = (By.XPATH, "//a[text()='Talent']/..")
    JOBS_TAB = (By.XPATH, "//a[text()='Jobs']/..")
    EVENTS_TAB = (By.XPATH, "//a[text()='Events']/..")
    PREMIUM_TAB = (By.XPATH, "//a[text()='Premium']/..")
    ABOUT_TAB = (By.XPATH, "//a[text()='About']/..")
    BLOG_TAB = (By.XPATH, "//a[text()='Blog']/..")
    FAQ_TAB = (By.XPATH, "//a[text()='FAQ']/..")
    VANHACK_PORTAL_TAB = (By.XPATH, "//a[text()='VanHack Portal']/..")

    NAVIGATION_FOOTER = "//footer"
    PRIVACY_POLICY_FOOTER_LINK = (By.XPATH, f"{NAVIGATION_FOOTER}//a[text()='Privacy policy']")
    TERMS_OF_USE_FOOTER_LINK = (By.XPATH, f"{NAVIGATION_FOOTER}//a[text()='Terms of use']")
    TALENT_FOOTER_LINK = (By.XPATH, f"{NAVIGATION_FOOTER}//a[text()='Talent']")
    GET_PREMIUM_FOOTER_LINK = (By.XPATH, f"{NAVIGATION_FOOTER}//a[text()='Get Premium']")
    BLOG_FOOTER_LINK = (By.XPATH, f"{NAVIGATION_FOOTER}//a[text()='Blog']")
    FAQ_FOOTER_LINK = (By.XPATH, f"{NAVIGATION_FOOTER}//a[text()='FAQ']")

    # endregion

    # region Check actions
    def check_tabs_displayed(self, expected_header_tabs_name=None):
        if not expected_header_tabs_name:
            expected_header_tabs_name = ["Employers",
                                       "Talent Pool",
                                       "Events",
                                       "Jobs",
                                       "Premium",
                                       "About",
                                       "Blog",
                                       "FAQ",
                                       "Login"]

        actual_header_tab_elements = self.find_all_elements(self.ALL_HEADER_TABS)
        actual_header_tabs = []
        for tab in actual_header_tab_elements:
            actual_header_tabs.append(tab.text)

        pytest.assume(expected_header_tabs_name == actual_header_tabs, "Navigation Tabs are not as expected")

        return self

    def check_privacy_policy_footer_link(self, expected_href):
        link_displayed = self.find_element(self.PRIVACY_POLICY_FOOTER_LINK)
        is_dislayed = link_displayed.is_displayed()
        if not is_dislayed:
            pytest.assume(is_dislayed is True, "PRIVACY POLICY footer link not displayed")
        else:
            actual_link = link_displayed.get_attribute("href")

            pytest.assume(actual_link == expected_href,
                          f"PRIVACY POLICY footer link is not as expected. Expected: {expected_href}, but was {actual_link}")

        return self

    def check_terms_of_use_footer_link(self, expected_href):
        link_displayed = self.find_element(self.TERMS_OF_USE_FOOTER_LINK)
        is_dislayed = link_displayed.is_displayed()
        if not is_dislayed:
            pytest.assume(is_dislayed is True, "TERMS OF USE footer link not displayed")
        else:
            actual_link = link_displayed.get_attribute("href")

            pytest.assume(actual_link == expected_href,
                          f"TERMS OF USE footer link is not as expected. Expected: {expected_href}, but was {actual_link}")

        return self

    def check_talent_company_footer_link(self, expected_href):
        link_displayed = self.find_element(self.TALENT_FOOTER_LINK)
        is_dislayed = link_displayed.is_displayed()
        if not is_dislayed:
            pytest.assume(is_dislayed is True, "TALENT footer link not displayed")
        else:
            actual_link = link_displayed.get_attribute("href")

            pytest.assume(actual_link == expected_href,
                          f"TALENT footer link is not as expected. Expected: {expected_href}, but was {actual_link}")

        return self

    def check_get_premium_company_footer_link(self, expected_href):
        link_displayed = self.find_element(self.GET_PREMIUM_FOOTER_LINK)
        is_dislayed = link_displayed.is_displayed()
        if not is_dislayed:
            pytest.assume(is_dislayed is True, "GET PREMIUM footer link not displayed")
        else:
            actual_link = link_displayed.get_attribute("href")

            pytest.assume(actual_link == expected_href,
                          f"GET PREMIUM footer link is not as expected. Expected: {expected_href}, but was {actual_link}")

        return self

    def check_blog_company_footer_link(self, expected_href):
        link_displayed = self.find_element(self.BLOG_FOOTER_LINK)
        is_dislayed = link_displayed.is_displayed()
        if not is_dislayed:
            pytest.assume(is_dislayed is True, "BLOG footer link not displayed")
        else:
            actual_link = link_displayed.get_attribute("href")

            pytest.assume(actual_link == expected_href,
                          f"BLOG footer link is not as expected. Expected: {expected_href}, but was {actual_link}")

        return self

    def check_faq_company_footer_link(self, expected_href):
        link_displayed = self.find_element(self.FAQ_FOOTER_LINK)
        is_dislayed = link_displayed.is_displayed()
        if not is_dislayed:
            pytest.assume(is_dislayed is True, "FAQ footer link not displayed")
        else:
            actual_link = link_displayed.get_attribute("href")

            pytest.assume(actual_link == expected_href,
                          f"FAQ footer link is not as expected. Expected: {expected_href}, but was {actual_link}")

        return self
    # endregion

    # region Scenarios
    def verify_privacy_policy_and_terms_of_use_footer_links(self, expected_links):
        self.check_privacy_policy_footer_link(expected_links.get("privacy policy"))
        self.check_terms_of_use_footer_link(expected_links.get("terms of use"))

        return self

    def verify_company_footer_links(self, expected_links):
        self.check_talent_company_footer_link(expected_links.get("talent"))
        self.check_get_premium_company_footer_link(expected_links.get("get premium"))

        self.check_blog_company_footer_link(expected_links.get("blog"))
        self.check_faq_company_footer_link(expected_links.get("faq"))

        return self
    # endregion
