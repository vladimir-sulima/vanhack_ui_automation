import allure

from VanHack_WebApp.pages.StartPage import StartPage


@allure.story("employer_screen")
def test_employers_page_defaults(browser):
    StartPage(browser)\
        .click_employers_tab() \
        .check_tabs_displayed()\
        .check_browse_the_vanhack_talent_pool_button_displayed()\
        .verify_employer_newsletter_section_defaults()

