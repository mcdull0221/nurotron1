__author__ = 'songxiaolin'
from page.login_page import LoginPage


class LoginHandle:
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)

    def send_account_key(self, user):
        """输入用户名"""
        self.login_page.account().send_keys(user)

    def clear_account(self):
        self.login_page.account().clear()

    def send_password(self, password):
        self.login_page.password().send_keys(password)

    def clear_password(self):
        self.login_page.password().clear()

    def click_login(self):
        self.login_page.login().click()

    def get_toast(self, message):
        toast_element = self.login_page.get_element(self, message)
        if toast_element:
            return True
        else:
            return False
