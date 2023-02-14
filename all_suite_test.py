import unittest

from unittest.loader import makeSuite

from test_cases.add_a_match import TestAddAMatch
from test_cases.add_a_player import TestAddAPlayer
from test_cases.change_the_language import TestChangeTheLanguage
from test_cases.edit_the_player import TestEditThePlayer
from test_cases.login_to_the_system import TestLoginPage
from test_cases.logout_of_the_system import TestLogoutPage


def full_suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(makeSuite(TestLoginPage))
    test_suite.addTest(makeSuite(TestLogoutPage))
    test_suite.addTest(makeSuite(TestEditThePlayer))
    test_suite.addTest(makeSuite(TestChangeTheLanguage))
    test_suite.addTest(makeSuite(TestAddAPlayer))
    test_suite.addTest(makeSuite(TestAddAMatch))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(full_suite())
