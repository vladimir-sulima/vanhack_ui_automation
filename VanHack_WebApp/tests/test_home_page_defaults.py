import allure

from VanHack_WebApp.pages.StartPage import StartPage


@allure.story("home_screen")
def test_navigation_tabs_dispalyed(browser):
    expected_tabs = ["Employers",
                     "Talent",
                     "Jobs",
                     "Events",
                     "Premium",
                     "About",
                     "Blog",
                     "FAQ",
                     "VanHack Portal"]

    StartPage(browser)\
        .check_tabs_displayed(expected_tabs)

@allure.story("home_screen")
def test_social_network_links_displayed(browser):
    expected_social_network_links = {"linkedin": f"https://www.linkedin.com/company/vanhack/",
                                    "twitter": "https://twitter.com/GoVanHack",
                                    "facebook": "https://www.facebook.com/govanhack/",
                                    "instagram": "https://www.instagram.com/govanhack/"}

    StartPage(browser)\
        .verify_social_network_links(expected_social_network_links)



