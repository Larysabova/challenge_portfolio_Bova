import time
from pages.base_page import BasePage


class AddAPlayer(BasePage):
    add_player_button_xpath = "//div[2]/div/div/a"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel"

    def title_of_page(self):
        assert self.get_page_title(self.login_url) == self.expected_title
