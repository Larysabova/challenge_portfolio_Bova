import os
import time
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.edit_the_player_page import EditThePlayer
from pages.login_page import LoginPage
from pages.add_a_player import AddAPlayer
from pages.add_match_form import AddAMatchForm
from pages.matches_page import Matches
from pages.players_page import Players
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddAMatch(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_a_match(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_will_be_clicable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_players_button()
        players_page = Players(self.driver)
        players_page.click_on_the_filter_button()
        players_page.type_in_name('Bora')
        players_page.type_in_surname('Lava')
        players_page.wait_for_button_will_be_clicable()
        players_page.click_on_the_close_filter_button()
        players_page.click_on_the_filtering_result()
        edit_the_player_page = EditThePlayer(self.driver)
        edit_the_player_page.title_of_page()
        edit_the_player_page.click_on_the_matches_button()
        matches_page = Matches(self.driver)
        matches_page.title_of_page()
        matches_page.click_on_the_add_match_button()
        add_a_match_form = AddAMatchForm(self.driver)
        add_a_match_form.title_of_page()
        add_a_match_form.type_in_my_team('Larifa')
        add_a_match_form.type_in_enemy_team('Timfa')
        add_a_match_form.type_in_my_team_score('3')
        add_a_match_form.type_in_enemy_team_score('2')
        add_a_match_form.type_in_date('05.02.2023')
        add_a_match_form.click_on_the_submit_button()
        matches_page.wait_for_visibility_of_popup()

        BasePage.tearDown(self)
