import time
__author__ = 'songxiaolin'
from util.get_by_local import GetByLocal
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
"""
封装操作Excel的方法
"""


class ActionMethod:
    def __init__(self, page, driver):
        self.driver = driver
        self.get_by_local = GetByLocal(self.driver)
        self.page = page

    def get_page(self, key):
        element = self.get_by_local.get_element(key, self.page)
        return element

    def input(self, *args):
        """输入值"""
        # element = self.get_by_local.get_element(args[0])
        element = self.get_page(args[0])
        if element is None:
            return "元素没找到"
        element.send_keys(args[1])

    def on_click(self, *args):
        """点击元素"""
        # element = self.get_by_local.get_element(args[0])
        element = self.get_page(args[0])
        if element is None:
            return "元素没找到"
        element.click()

    def sleep_time(self, *args):
        sleep(int(args[0]))

    def get_size(self, *args):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self, *args):
        # [x , y]
        x1 = self.get_size()[0]/10*8
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x2, y1, 500)

    # 向右滑动
    def swipe_right(self, *args):
        # [x , y]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10 * 8
        self.driver.swipe(x1, y1, x2, y1, 500)

    # 向下滑动
    def swipe_down(self, *args):
        # [x , y]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 3
        y2 = self.get_size()[0] / 10 * 8
        self.driver.swipe(x1, y1, x1, y2, 500)

    def get_element(self, *args):
        sleep(1)
        element = self.get_page(args[0])
        if element is None:
            return None
        return element

    def get_toast_element(self, *args):
        """
        获取toast element
        """
        sleep(2)
        toast_element = ("xpath", "//*[contains(@text," + args[0] + ")]")
        return WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.presence_of_element_located(toast_element))
