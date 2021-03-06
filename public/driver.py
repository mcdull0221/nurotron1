__author__ = 'songxiaolin'
from appium import webdriver
import time
from util.write_user_command import WriteUserCommand
import sys,os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class BaseDriver:
    def __init__(self):
        self.write_file = WriteUserCommand()

    def android_driver(self, i):
        deviceName = self.write_file.get_value('user_info_'+str(i), 'deviceName')
        port = self.write_file.get_value('user_info_'+str(i), 'port')
        desired_caps = {
            'platformName': 'Android',
            # 'platformVersion': '7.1.2',
            'deviceName': deviceName,
            # 自动确定确定应用权限
            'autoGrantPermissions': 'true',
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true',
            'automationName': 'Uiautomator2',
            # 'app': 'E:\\pythonProject\\appiumTest\\nurotron\APP\\app-debug.apk',
            'app': PATH('../app/app-debug.apk'),        # 不会覆盖安装
            'noReset': 'true'
        }
        driver = webdriver.Remote('http://localhost:'+str(port)+'/wd/hub', desired_caps)
        time.sleep(10)
        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        pass
