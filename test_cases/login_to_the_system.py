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


class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        # self.driver_service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts.futbolkolektyw.pl/en/')  # Open the website
        self.driver.fullscreen_window()  # Open a browser window in full-size mode
        self.driver.implicitly_wait(IMPLICITLY_WAIT)  # Wait before you start testing

    def test_log_in_to_the_system(self):
        user_login = LoginPage(self.driver)
        # user_login.title_of_page()  # Check if the title of the open page is correct
        user_login.type_in_email('user01@getnada.com')  # Enter "user01@getnada.com" in the mail field
        user_login.type_in_password('Test-1234')  # Enter "Test-1234" in the password field
        user_login.wait_for_button_will_be_clickable()  # Wait for the button to be clickable
        user_login.click_on_the_sign_in_button()  # Click on the signin button
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()  # Check if the title of the open page is correct

        BasePage.take_a_screenshot(self, 'TC001.png')  # Take a screenshot

        BasePage.tearDown(self)  # Close the browser after the test
