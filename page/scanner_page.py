__author__ = 'songxiaolin'
from testSet.public.driver import BaseDriver
from util.get_by_local import GetByLocal


class scannerPage:
    def __init__(self, i):
        get_driver = BaseDriver()
        self.driver = get_driver.android_driver(i)
        self.get_by_local = GetByLocal(self.driver)

    def get_bleAlert_ok(self):
        ''' 提示打开蓝牙弹出框的确定元素 '''
        return self.get_by_local.get_element('bleok')

    def get_location_ok(self):
        ''' 弹出定位权限弹出框的确定元素 '''
        return self.get_by_local.get_element('locationOk')

    def get_driver(self):
        ''' 已找到的设备 '''
        return self.get_by_local.get_element('driverList')

    def get_driver_ok(self):
        ''' 当点击已找到的设备会有二次对话框，返回确定元素 '''
        return self.get_by_local.get_element('connectSure')

    def get_page_source(self):
        """
        获取页面所有元素
        :return: scannerpage
        """
        scannerpage = self.driver.page_source
        return scannerpage
