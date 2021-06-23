from CGUITF.tools.util import Utility


class MainMenu:

    def __init__(self):

        self.main_menu_ele = Utility.get_json("..\\conf\\ele.conf")
        print(self.main_menu_ele)

    def click_logout(self,driver):
        logout_link = driver.find_element(self.main_menu_ele[4]['prop'], self.main_menu_ele[4]['value'])
        logout_link.click()

if __name__ == '__main__':
    MainMenu()


