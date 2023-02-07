from pages.base_page import BasePage


class EditThePlayer(BasePage):
    level_filter_field_xpath = "//*[@name='level']"
    submit_button_xpath = "//button[@type='submit']"
    edit_players_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Edit player Bora Lava"
    saved_player_popup = "//*[text()='Saved player.']"
    matches_button_xpath = "//*[text()='Matches']"

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.submit_button_xpath)
        assert self.get_page_title(self.edit_players_url) == self.expected_title

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_matches_button(self):
        self.click_on_the_element(self.matches_button_xpath)

    def type_in_level(self, level):
        self.field_send_keys(self.level_filter_field_xpath, level)

    def wait_for_button_will_be_clicable(self):
        self.wait_for_element_to_be_clicable(self.submit_button_xpath)

    def wait_for_visibility_of_element(self):
        self.wait_for_visibility_of_element_located(self.saved_player_popup)
