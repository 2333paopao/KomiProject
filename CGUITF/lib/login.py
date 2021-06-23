from CGUITF.tools.util import Utility

class Login:

    def __init__(self):
        self.driver = Utility.get_driver('..\\conf\\base.conf')
        self.login_ele = Utility.get_json("..\\conf\\ele.conf")

    def input_account(self,username):
        uname = self.driver.find_element(self.login_ele[0]['prop'], self.login_ele[0]['value'])
        Utility.input(uname, username)

    def input_password(self,password):
        upass = self.driver.find_element(self.login_ele[1]['prop'], self.login_ele[1]['value'])
        Utility.input(upass, password)

    def input_verifycode(self,verifycode):
        vfcode = self.driver.find_element(self.login_ele[2]['prop'], self.login_ele[2]['value'])
        Utility.input(vfcode, verifycode)

    def click_login_button(self):
        login_button = self.driver.find_element(self.login_ele[3]['prop'], self.login_ele[3]['value'])
        login_button.click()

    def login(self,login_data):
        self.input_account(login_data['username'])
        self.input_password(login_data['password'])
        self.input_verifycode(login_data['verifycode'])
        self.click_login_button()

