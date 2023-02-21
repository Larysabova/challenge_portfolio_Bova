from webdriver_manager.core import driver

from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class Matches(BasePage):
    add_match_button_xpath = "//main/a/button/span[1]"
    matches_url = ('https://scouts.futbolkolektyw.pl/en/')
    expected_title = "Matches player Bora Lava"
    added_match_popup_xpath = "//*[text() = 'Added match.']"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.add_match_button_xpath)
        assert self.get_page_title(self.matches_url) == self.expected_title

    def click_on_the_add_match_button(self):
        self.click_on_the_element(self.add_match_button_xpath)

    def wait_for_visibility_of_popup(self):
        self.wait_for_visibility_of_element_located(self.added_match_popup_xpath)

    def wait_for_button_will_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.add_match_button_xpath)
