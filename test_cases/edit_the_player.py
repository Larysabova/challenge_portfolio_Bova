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
from pages.players_page import Players
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestEditThePlayer(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_edit_the_player(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_will_be_clickable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_button_will_be_clickable()
        dashboard_page.click_on_the_players_button()
        players_page = Players(self.driver)
        players_page.click_on_the_filter_button()
        players_page.type_in_name('Bora')
        players_page.type_in_surname('Lava')
        players_page.click_on_the_close_filter_button()
        players_page.wait_for_button_will_be_clickable()
        players_page.click_on_the_result_of_filtering()
        edit_the_player_page = EditThePlayer(self.driver)
        edit_the_player_page.title_of_page()
        edit_the_player_page.type_in_level('Pro')
        edit_the_player_page.wait_for_button_will_be_clickable()
        edit_the_player_page.click_on_the_submit_button()
        edit_the_player_page.wait_for_visibility_of_element()

        BasePage.take_a_screenshot(self, 'TC005.png')

        BasePage.tearDown(self)
