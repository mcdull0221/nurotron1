import logging

__author__ = 'songxiaolin'
from Handle.scanner_handle import scannerHandle
from testSet.public.swipe import swipe
from time import sleep

class scannerBusiness:
    def __init__(self,driver):
        self.scanner_handle =scannerHandle(driver)
        self.swipe = swipe(driver)

    def connect_devices(self):
        try:
            self.scanner_handle.click_ble_ok()
            sleep(2)
            self.scanner_handle.click_location_ok()
            sleep(2)
        except:
            logging.info('未发现蓝牙弹框')
            pass

    def devices_nofound(self):
        self.connect_devices()
        for i in range(1, 11):
            sleep(1)
            page = self.driver.page_source
            if page.__contains__('设备查找中'):
                sleep(6)
                page1 = self.driver.page_source
                if page1.__contains__('00:02:5B'):
                    self.scanner_handle.click_driver()
                    sleep(2)
                    self.scanner_handle.click_driver_ok()
                    return True
                    break
                
