__author__ = 'songxiaolin'
from page.scanner_page import scannerPage


class ScannerHandle:
    def __init__(self, driver):
        self.driver = driver
        self.scanner_page = scannerPage(driver)

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

    def chack_page_source(self, value):
        """查询页面是否包含某个元素"""
        page_source = self.scanner_page.get_page_source()
        if page_source.__contains__(value):
            return True
        else:
            return False

    def swipe_down(self):
        self.scanner_page.swipe_down()

if __name__ == '__main__':
    scanner_handle = ScannerHandle(0)
    page_source = scanner_handle.chack_page_source("00:02:5B")
    print(page_source)
