from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    menu_button_xpath = "//button[@aria-label='menu']"
    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    current_player_hyperlink_xpath = "//ul[2]/div[1]/div[2]/span"
    language_button_xpath = "//*[text()='English' or text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    matches_button_xpath = "//*[text()='Matches']"
    reports_button_xpath = "//*[text()='Reports']"
    my_team_field_xpath = "//*[@name='myTeam']"
    enemy_team_field_xpath = "//*[@name='enemyTeam']"
    my_team_score_field_xpath = "//*[@name='myTeamScore']"
    enemy_team_score_field_xpath = "//*[@name='enemyTeamScore']"
    date_field_xpath = "//*[@name='date']"
    match_at_home_field_xpath = "//span[text()='Match at home']/preceding::input[1]"
    match_out_home_field_xpath = "//span[text()='Match out home']/preceding::input[1]"
    tshirt_color_field_xpath = "//*[@name='tshirt']"
    league_field_xpath = "//*[@name='league']"
    time_played_field_xpath = "//*[@name='timePlayed']"
    number_field_xpath = "//*[@name='number']"
    web_match_field_xpath = "//*[@name='webMatch']"
    general_field_xpath = "//*[@name='general']"
    rating_field_xpath = "//*[@name='rating']"
    submit_button_xpath = "//button[@type='submit']"
    clear_button_xpath = "//button[contains(@class, 'containedSecondary')]"
    add_match_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Adding match player Bora Lava"

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.submit_button_xpath)
        assert self.get_page_title(self.add_match_url) == self.expected_title

    def type_in_my_team(self, my_team):
        self.field_send_keys(self.my_team_field_xpath, my_team)

    def type_in_enemy_team(self, enemy_team):
        self.field_send_keys(self.enemy_team_field_xpath, enemy_team)

    def type_in_my_team_score(self, my_team_score):
        self.field_send_keys(self.my_team_score_field_xpath, my_team_score)

    def type_in_enemy_team_score(self, enemy_team_score):
        self.field_send_keys(self.enemy_team_score_field_xpath, enemy_team_score)

    def type_in_date(self, date):
        self.field_send_keys(self.date_field_xpath, date)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def wait_for_button_will_be_clicable(self):
        self.wait_for_element_to_be_clicable(self.submit_button_xpath)
