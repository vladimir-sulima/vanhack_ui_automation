import pytest

from VanHack_WebApp.pages.CommonElements_Abstract import CommonElements
from framework.WebDriverWrapper import WebDriverWrapper
from selenium.webdriver.common.by import By


class EmployersPage(WebDriverWrapper, CommonElements):

    # region Locators
    ALL_HEADER_TABS = (By.XPATH, "//div[@class='NavigationPrimaryMenu']//ul//a")
    BROWSE_THE_VANHACK_TALENT_POOL = (By.XPATH, "//a[text()='Browse the VanHack Talent Pool']/..")

    EMPLOYER_NEWSLETTER_FORM_CONTENT = "//div[@class='_form-title' and text()='Employer Newsletter ']/../.."
    INPUT_FIELD = f"/following-sibling::div/input"
    FIRST_NAME_LABEL = f"{EMPLOYER_NEWSLETTER_FORM_CONTENT}//label[text()='First Name']"
    FIRST_NAME_INPUT_FIELD = f"{FIRST_NAME_LABEL}{INPUT_FIELD}"
    LAST_NAME_LABEL = f"{EMPLOYER_NEWSLETTER_FORM_CONTENT}//label[text()='Last Name']"
    LAST_NAME_INPUT_FIELD = f"{LAST_NAME_LABEL}{INPUT_FIELD}"
    EMAIL_LABEL = f"{EMPLOYER_NEWSLETTER_FORM_CONTENT}//label[text()='Email*']"
    EMAIL_INPUT_FIELD = f"{EMAIL_LABEL}{INPUT_FIELD}"
    SIGN_UP_BUTTON = f"{EMPLOYER_NEWSLETTER_FORM_CONTENT}//button[text()='Sign Up']"

    # endregion

    # region Check actions
    def check_browse_the_vanhack_talent_pool_button_displayed(self):
        is__browse_the_vanhack_talent_pool_button_displayed = \
            self.check_element_displayed(self.BROWSE_THE_VANHACK_TALENT_POOL)

        pytest.assume(is__browse_the_vanhack_talent_pool_button_displayed is True,
                      "BROWSE THE VANHACK TALENT POOL button not displayed - Employers page")

        return self

    def check_first_name_label_displayed_employer_newsletter_section(self):
        is_first_name_label_displayed = self.check_element_displayed(self.FIRST_NAME_LABEL, By.XPATH)

        pytest.assume(is_first_name_label_displayed is True,
                      "FIRST NAME label not displayed - Employer Newsletter section, Employers page")

        return self

    def check_last_name_label_displayed_employer_newsletter_section(self):
        is_first_name_label_displayed = self.check_element_displayed(self.LAST_NAME_LABEL, By.XPATH)

        pytest.assume(is_first_name_label_displayed is True,
                      "LAST NAME label not displayed - Employer Newsletter section, Employers page")

        return self

    def check_email_label_displayed_employer_newsletter_section(self):
        is_first_name_label_displayed = self.check_element_displayed(self.EMAIL_LABEL, By.XPATH)

        pytest.assume(is_first_name_label_displayed is True,
                      "EMAIL label not displayed - Employer Newsletter section, Employers page")

        return self

    def check_first_name_input_field_displayed_employer_newsletter_section(self):
        input_field = self.find_element(self.FIRST_NAME_INPUT_FIELD, By.XPATH)

        pytest.assume(input_field.is_displayed() is True, "FIRST NAME input field not displayed "
                                                          "- Employer Newsletter section, Employer page")
        pytest.assume(input_field.get_attribute("placeholder") == "Your first name",
                      "Placeholder for FIRST NAME input field is not as expected "
                      "- Employer Newsletter section, Employer page")

        return self

    def check_last_name_input_field_displayed_employer_newsletter_section(self):
        input_field = self.find_element(self.LAST_NAME_INPUT_FIELD, By.XPATH)

        pytest.assume(input_field.is_displayed() is True,
                      "LAST NAME input field not displayed - Employer Newsletter section, Employer page")
        pytest.assume(input_field.get_attribute("placeholder") == "Your last name",
                      "Placeholder for LAST NAME input field is not as expected "
                      "- Employer Newsletter section, Employer page")

        return self

    def check_email_input_field_displayed_employer_newsletter_section(self):
        input_field = self.find_element(self.EMAIL_INPUT_FIELD, By.XPATH)

        pytest.assume(input_field.is_displayed() is True,
                      "EMAIL input field not displayed - Employer Newsletter section, Employer page")
        pytest.assume(input_field.get_attribute("placeholder") == "Your email",
                      "Placeholder for EMAIL input field is not as expected"
                      " - Employer Newsletter section, Employer page")

        return self

    def check_sign_up_button_displayed_employer_newsletter_section(self):
        is_button_exist = self.check_element_displayed(self.SIGN_UP_BUTTON, By.XPATH)

        pytest.assume(is_button_exist is True, "SIGN UP button not displayed "
                                                "-  Employer Newsletter section, Employer page")
        return self
    # endregion

    def verify_employer_newsletter_section_defaults(self):
        self.check_first_name_label_displayed_employer_newsletter_section()
        self.check_first_name_input_field_displayed_employer_newsletter_section()
        self.check_last_name_label_displayed_employer_newsletter_section()
        self.check_last_name_input_field_displayed_employer_newsletter_section()
        self.check_email_label_displayed_employer_newsletter_section()
        self.check_email_input_field_displayed_employer_newsletter_section()
        self.check_sign_up_button_displayed_employer_newsletter_section()


