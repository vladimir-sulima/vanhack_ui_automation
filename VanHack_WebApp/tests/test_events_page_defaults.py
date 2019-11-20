import allure

from VanHack_WebApp.pages.StartPage import StartPage


@allure.story("events_screen")
def test_employers_page_defaults(browser):

    expected_footer_links = {
                             "privacy policy": "https://vanhack.com/privacy-policy",
                             "terms of use": "https://vanhack.com/terms-of-use",
                             "talent": f"https://vanhack.com/platform/#/talent",
                             "get premium": "https://vanhack.com/checkout",
                             "blog": "https://www.vanhack.com/blog/",
                             "faq": "https://www.vanhack.com/faq/"

    }

    StartPage(browser) \
        .click_events_tab() \
        .check_tabs_displayed()\
        .verify_privacy_policy_and_terms_of_use_footer_links(expected_footer_links)\
        .verify_company_footer_links(expected_footer_links)




