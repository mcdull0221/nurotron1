__author__ = 'songxiaolin'
from testSet.public.driver import AppiumTest


class swipe():
    # 获取屏幕的高和宽
    def __init__(self):
        driver = AppiumTest().get_driver()
        self.driver = driver

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
        y1 = self.get_size()[1] / 10 * 4
        y2 = self.get_size()[0] / 10 * 7
        self.driver.swipe(x1, y1, x1, y2, 500)


