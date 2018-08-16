__author__ = 'songxiaolin'
from appium import webdriver


class AppiumTest():
    def __init__(self):
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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver
