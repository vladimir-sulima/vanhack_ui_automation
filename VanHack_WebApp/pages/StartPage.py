import pytest
from selenium.webdriver.common.by import By
from VanHack_WebApp.pages.EmployersTab.EmployersPage import EmployersPage
from VanHack_WebApp.pages.EventsTab.EventsPage import EventsPage
from VanHack_WebApp.pages.CommonElements_Abstract import CommonElements
from framework.WebDriverWrapper import WebDriverWrapper


class StartPage(WebDriverWrapper, CommonElements):

    # region Locators
    LINKEDIN_LINK = (By.XPATH, "//img[@alt='LinkedIn']/..")
    TWITTER_LINK = (By.XPATH, "//img[@alt='Twitter']/..")
    FACEBOOK_LINK = (By.XPATH, "//img[@alt='Facebook']/..")
    INSTAGRAM_LINK = (By.XPATH, "//img[@alt='Instagran']/..")
    # endregion

    # region Click actions
    def click_employers_tab(self):
        self.find_and_click(self.EMPLOYERS_TAB)

        return EmployersPage(self.browser)

    def click_events_tab(self):
        self.find_and_click(self.EVENTS_TAB)

        return EventsPage(self.browser)
    # endregion

    # region Check actions
    def check_linkedin_link_displayed(self, expected_href):
        link = self.find_element(self.LINKEDIN_LINK)
        link_displayed = link.is_displayed()
        if not link_displayed:

            pytest.assume(link_displayed is True, "LINKED IN link not displayed - Start Page")
        else:
            actual_href = link.get_attribute("href")

            pytest.assume(actual_href == expected_href,
                      f"LINKED IN link is not as expected - Home page. Expected:{expected_href}, but was {actual_href}")

        return self

    def check_twitter_link_displayed(self, expected_href):
        link = self.find_element(self.TWITTER_LINK)
        link_displayed = link.is_displayed()

        if not link_displayed:
            pytest.assume(link_displayed is True, "TWITTER link not displayed - Start Page")
        else:
            actual_href = link.get_attribute("href")

            pytest.assume(actual_href == expected_href,
                      f"TWITTER link is not as expected - Home page. Expected:{expected_href}, but was {actual_href}")

        return self

    def check_facebook_link_displayed(self, expected_href):
        link = self.find_element(self.FACEBOOK_LINK)
        link_displayed = link.is_displayed()
        if not link_displayed:

            pytest.assume(link_displayed is True, "FACEBOOK link not displayed - Start Page")
        else:
            actual_href = link.get_attribute("href")

            pytest.assume(actual_href == expected_href,
                          f"FACEBOOK link is not as expected - Home page. Expected:{expected_href}, but was {actual_href}")

        return self

    def check_instagram_link_displayed(self, expected_href):
        link = self.find_element(self.INSTAGRAM_LINK)
        link_displayed = link.is_displayed()
        if not link_displayed:

            pytest.assume(link_displayed is True, "INSTAGRAM link not displayed - Start Page")
        else:
            actual_href = link.get_attribute("href")

            pytest.assume(actual_href == expected_href,
                          f"INSTAGRAM link is not as expected - Home page. Expected:{expected_href}, but was {actual_href}")

        return self
    # endregion

    # region Scenarios
    def verify_social_network_links(self, expected_links):
        self.check_linkedin_link_displayed(expected_links.get("linkedin"))
        self.check_twitter_link_displayed((expected_links.get("twitter")))
        self.check_facebook_link_displayed(expected_links.get("facebook"))
        self.check_instagram_link_displayed(expected_links.get("instagram"))

        return self
# endregion
