__author__ = 'songxiaolin'
from page.scanner_page import scannerPage


class scannerHandle:
    def __init__(self, i):
        self.scanner_page = scannerPage(i)

    def click_ble_ok(self):
        ''' 提示打开蓝牙弹出框点击确认按钮'''
        self.scanner_page.get_bleAlert_ok().click()

    def click_location_ok(self):
        ''' 弹出定位权限弹出框点击确认按钮 '''
        self.scanner_page.get_location_ok().click()

    def click_driver(self):
        ''' 点击已找到的设备 '''
        self.scanner_page.get_driver().click()

    def click_driver_ok(self):
        ''' 确认连接设备 '''
        self.scanner_page.get_driver_ok().click()
