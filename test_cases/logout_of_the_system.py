import os
import time
import unittest

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

from pages.base_page import BasePage
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLogoutPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_log_out_of_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user01@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_button_will_be_clickable()
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.wait_for_button_will_be_clickable()
        dashboard_page.click_on_the_sign_out_button()
        user_login.wait_for_button_will_be_clickable()


        BasePage.take_a_screenshot(self, 'TC002.png')

        BasePage.tearDown(self)
