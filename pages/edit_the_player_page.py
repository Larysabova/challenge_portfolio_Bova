import time

from pages.base_page import BasePage


class EditThePlayer(BasePage):
    menu_button_xpath = "//button[@aria-label='menu']"
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    current_player_xpath = "//ul[2]/div[1]/div[2]/span"
    language_button_xpath = "//*[text()='English' or text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    matches_button_xpath = "//*[text()='Matches']"
    reports_button_xpath = "//*[text()='Reports']"
    title_of_box_xpath = "//span[text()='Edit player Sova Lara']"
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@name='name']"
    surname_field_xpath = "//*[@name='surname']"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@name='weight']"
    height_field_xpath = "//*[@name='height']"
    age_field_xpath = "//*[@name='age']"
    leg_field_xpath = "//div[contains(@id, 'select - leg')]"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name = 'level']"
    main_position_field_xpath = "//*[@name='mainPosition']"
    district_field_xpath = "//div[contains(@id, 'select - district')]"
    achievements_field_xpath = "//*[@name = 'achievements']"
    Add_language_button_xpath = "//button[@aria-label = 'Add language']"
    Łączy_nas_piłka_field_xpath = "//*[@name='webLaczy']"
    nineteen_minute_field_xpath = "//*[@name='web90']"
    facebook_field_xpath = "//*[@name='webFB']"
    # ex_club_field_xpath = "//*[@name='exClub']"
    add_link_to_Youtube_button_xpath = "//button[contains(@aria-label,'Youtube')]"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[contains(@class, 'containedSecondary')]"
    edit_players_url = ('https://scouts.futbolkolektyw.pl/en/')
    expected_title = "Edit player Bora Lava"
    # expected_level_value = "Pro"
    # expected_ex_club_value = "Timfa"
    saved_player_popup = "//*[text()='Saved player.']"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.current_player_xpath)
        assert self.get_page_title(self.edit_players_url) == self.expected_title

    # def value_of_ex_club(self):
    #     self.wait_for_visibility_of_element_located(self.title_of_box_xpath)
    #     expected_text = self.expected_ex_club_value
    #     self.assert_element_text(self.ex_club_field_xpath, expected_text)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_matches_button(self):
        self.click_on_the_element(self.matches_button_xpath)

    def click_on_the_current_player_button(self):
        self.click_on_the_element(self.current_player_xpath)

    def type_in_level(self, level):
        self.field_send_keys(self.level_field_xpath, level)

    # def type_in_ex_club(self, exClub):
    #     self.field_send_keys(self.ex_club_field_xpath, exClub)

    def wait_for_button_will_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)

    def wait_for_visibility_of_element(self):
        self.wait_for_visibility_of_element_located(self.saved_player_popup)
