__author__ = 'songxiaolin'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    """
    封装页面的公共方法
    """
    def __init__(self, driver):
        self.driver = driver
        # get_driver = BaseDriver()
        # self.driver = get_driver.android_driver(i)

    def get_page_source(self):
        """
        获取页面所有元素
        :return: page_source
        """
        page_source = self.driver.page_source
        return page_source

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
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 向右滑动
    def swipe_right(self):
        # [x , y]
        x1 = self.get_size()[0] / 10
        y1 = self.get_size()[1] / 2
        x2 = self.get_size()[0] / 10 * 8
        self.driver.swipe(x1, y1, x2, y1, 1000)

    # 向下滑动
    def swipe_down(self):
        # [x , y]
        x1 = self.get_size()[0] / 2
        y1 = self.get_size()[1] / 10 * 2
        y2 = self.get_size()[0] / 10 * 9
        self.driver.swipe(x1, y1, x1, y2, 1000)

    def get_toast_element(self, message):
        '''
        获取tostelement
        '''
        toast_element = ("xpath", "//*[contains(@text," + message + ")]")
        toast = WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.presence_of_element_located(toast_element))
        return toast


if __name__ == '__main__':
    base_page = BasePage(0)
    size = base_page.get_size()
    print(size)
