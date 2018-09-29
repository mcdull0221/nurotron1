__author__ = 'songxiaolin'
from page.base_page import BasePage
from util.get_by_local import GetByLocal


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)
        # self.driver = self.base_page.driver
        self.get_by_local = GetByLocal(self.driver)

    def get_element(self, key, section='login_element'):
        return self.get_by_local.get_element(key, section)

    def account(self):
        self.get_element('account')

    def password(self):
        self.get_element('password')

    def forget(self):
        self.get_element('forget')

    def login(self):
        self.get_element('login')

    def register(self):
        self.get_element('register')

    def skip(self):
        self.get_element('skip')

    def toast_element(self, message):
        toast = self.base_page.get_toast_element(message)
        return toast
