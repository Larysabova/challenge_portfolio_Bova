from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    remind_password_hyperlink_xpath = "//*[text()='Remind password']"
    select_language_button = "//*[@role='button']"
    sign_in_button_xpath = "//*[text()='Sign in']"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sign in"
    title_of_box_xpath = "//h5[text()='Scouts Panel']"
    header_of_box = 'Scouts Panel'

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_on_the_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.sign_in_button_xpath)
        assert self.get_page_title(self.login_url) == self.expected_title

    def element_text(self):
        expected_text = self.header_of_box
        self.assert_element_text(self.title_of_box_xpath, expected_text)

    def wait_for_button_will_be_clicable(self):
        self.wait_for_element_to_be_clicable(self.sign_in_button_xpath)
