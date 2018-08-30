import time

__author__ = 'songxiaolin'
from util.get_by_local import GetByLocal
from testSet.public.driver import BaseDriver
"""
封装操作Excel的方法
"""


class ActionMethod:
    def __init__(self):
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.get_by_local = GetByLocal(self.driver)

    def input(self, element_key, value):
        """输入值"""
        element = self.get_by_local.get_element(element_key)
        if element == None:
            return element_key, "元素没找到"
        element.send_keys(value)

    def on_click(self, element_key):
        """点击元素"""
        element = self.get_by_local.get_element(element_key)
        if element == None:
            return element_key, "元素没找到"
        element.click()

    def sleep_time(self, value):
        time.sleep(value)

    def get_size(self):
        size = self.driver.get_window_size()
        width = size['width']
        height = size['height']
        return width, height

    # 向左滑动
    def swipe_left(self):
        # [x , y]
        x1 = self.get_size()[0]/10*8
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10
        self.driver.swipe(x1, y1, x2, y1, 500)

    # 向右滑动
    def swipe_right(self):
        # [x , y]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10 * 8
        self.driver.swipe(x1, y1, x2, y1, 500)

    # 向下滑动
    def swipe_down(self):
        # [x , y]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 3
        y2 = self.get_size()[0] / 10 * 8
        self.driver.swipe(x1, y1, x1, y2, 500)
