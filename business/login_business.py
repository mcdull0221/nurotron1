__author__ = 'songxiaolin'
from Handle.login_handle import LoginHandle
from time import sleep


class LoginBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.login_handle = LoginHandle(self.driver)

    def login_user_error(self):
        self.login_handle.send_account_key('13333333333')
        self.login_handle.send_password('s1234567')
        self.login_handle.click_login()
        user_flag = self.login_handle.get_toast('用户名与密码不符，请确认后重试。')
        if user_flag:
            return True
        else:
            return False

    def login_success(self):
        self.login_handle.send_account_key('14100000001')
        self.login_handle.send_password('s1234567')
        self.login_handle.click_login()
        try:
            if self.login_handle.get_message() is not None:
                self.login_handle.click_unlock_pattern_no()
                sleep(2)
                return True
        except:
            return False

