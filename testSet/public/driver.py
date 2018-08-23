__author__ = 'songxiaolin'
from appium import webdriver
import time


class BaseDriver:
    def android_driver(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': '298384e47d74',
            # 不需要用appActivity启动，有时会报错。
            'app': 'E:\\app-debug.apk',
            'udid': '298384e47d74',
            # 自动确定确定应用权限
            'autoGrantPermissions': 'true',
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true',
            'automationName': 'Uiautomator2',
        }
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(10)
        return driver

    def ios_driver(self):
        pass

    def get_driver(self):
        pass
