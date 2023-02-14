import time
from pages.base_page import BasePage


class AddAPlayer(BasePage):
    menu_button_xpath = "//button[@aria-label='menu']"
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    language_button_xpath = "//*[text()='English' or text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    matches_button_xpath = "//*[text()='Matches']"
    reports_button_xpath = "//*[text()='Reports']"
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
    add_link_to_Youtube_button_xpath = "//button[contains(@aria-label,'Youtube')]"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[contains(@class, 'containedSecondary')]"
    add_player_url = ('https://scouts-test.futbolkolektyw.pl/en/players/add')
    expected_title = "Add player"
    added_player_popup_xpath = "//*[text() = 'Added player.']"

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

    def wait_for_button_will_be_clickable(self):
        self.wait_for_element_to_be_clickable(self.submit_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.name_field_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.surname_field_xpath, surname)

    def type_in_age(self, date_of_birth):
        self.field_send_keys(self.age_field_xpath, date_of_birth)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_field_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def wait_for_visibility_of_popup(self):
        self.wait_for_visibility_of_element_located(self.added_player_popup_xpath)
