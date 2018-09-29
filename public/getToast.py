__author__ = 'songxiaolin'
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import logging
import time


# 获取页面toast
def _find_toast(message, timeout, poll_frequency, driver):
    message = '//*[@text=\'{}\']'.format(message)
    element = WebDriverWait(driver, timeout, poll_frequency).until(
        expected_conditions.presence_of_element_located((By.XPATH, message)))
    return element
    # self._find_toast('Hello selendroid toast!',10,0.5,self.driver) 来调用


def get_toast_element(self, message):
    '''
    获取tostelement
    '''
    time.sleep(2)
    toast_element = ("xpath", "//*[contains(@text," + message + ")]")
    toast = WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.presence_of_element_located(toast_element))
    print(toast)
    return toast


def get_toast(self, message):  # 查找toast值
    '''
    method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
    parameter explain：【text】查找的toast值
    Usage:
        device.get_Toast('再按一次退出iBer')
    '''
    logging.info("查找toast值---'%s'" % (message))
    try:
        message = '//*[@text=\'{}\']'.format(message)
        ele = WebDriverWait(self.driver, 10, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, message)))
        logging.info("查找到toast----%s" % message)
        return ele.get_attribute("text")

    except:
        logging.error("未查找到toast----%s" % message)
        return False

