from webdriver_manager.core import driver

from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait


class Dashboard(BasePage):
    header_of_box = "//header/div/h6"
    menu_button_xpath = "//button[@aria-label='menu']"
    main_page_button_xpath = "//*[text()='Main page']"
    main_page_button_in_Polish_xpath = "//*[text()='Strona główna']"
    players_button_xpath = "//*[text()='Players']"
    language_button_xpath = "//ul[2]/div[1]"
    sign_out_button_xpath = "//*[text()='Sign out']"
    dev_team_contact_button_xpath = "//*[1][name() = 'a']"
    add_player_button_xpath = "//*[2][name() = 'a']"
    last_created_player_hyperlink_xpath = "//*[3][name() = 'a']/button/span[1]"
    last_updated_player_hyperlink_xpath = "//a[2]/button/span[1]"
    last_created_match_hyperlink_xpath = "//a[3]/button/span[1]"
    last_updated_match_hyperlink_xpath = "//a[4]/button/span[1]"
    last_updated_report_hyperlink_xpath = "//a[5]/button/span[1]"
    expected_title = "Scouts panel"
    dashboard_url = ('https://scouts.futbolkolektyw.pl/en/')
    wait = WebDriverWait(driver, 10)

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.header_of_box)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def wait_for_button_will_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.sign_out_button_xpath)

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def click_on_the_sign_out_button(self):
        self.click_on_the_element(self.sign_out_button_xpath)

    def click_on_the_language_button(self):
        self.click_on_the_element(self.language_button_xpath)

    def wait_for_visibility_of_button_in_polish(self):
        self.wait_for_visibility_of_element_located(self.main_page_button_in_Polish_xpath)

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)
