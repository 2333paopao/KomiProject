from lib.login import Login
from lib.main_menu import MainMenu
from tools.util import Utility
import time

class LoginTest:

    def __init__(self):
        self.login = Login()
        self.menu = MainMenu()

    def test_login(self):
        login_info = Utility.get_xls('..\\testdata\\woniusales_test_cases.xlsx','login',1,6,3,4)
        for info in login_info:
            self.login.login(info)
            if Utility.is_element_present(self.login.driver,'link text','注销'):
                actual = 'login-pass'
                time.sleep(2)
                self.menu.click_logout(self.login.driver)
            else:
                actual = 'login-fail'
                time.sleep(2)
                self.login.driver.refresh()

            if Utility.assert_equal(info['expect'],actual):
                print('login test pass')
            else:

                print('login test fail')

if __name__ == '__main__':
    LoginTest().test_login()