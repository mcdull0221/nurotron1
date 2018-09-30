__author__ = 'songxiaolin'
import logging
from Handle.scanner_handle import ScannerHandle
from time import sleep


class ScannerBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.scanner_handle = ScannerHandle(self.driver)

    def connect_devices(self):
        try:
            self.scanner_handle.click_ble_ok()
            sleep(2)
        except:
            # try:
            #     self.scanner_handle.click_location_ok()
            #     sleep(2)
            # except:
            #     pass
            pass

    @property
    def devices_found(self):
        self.connect_devices()
        for i in range(1, 11):
            sleep(10)
            if self.scanner_handle.chack_page_source("00:02:5B") is True:
                self.scanner_handle.click_driver()
                sleep(2)
                self.scanner_handle.click_driver_ok()
                return True
            elif self.scanner_handle.chack_page_source("设备查找中") is True:
                logging.info("设备查找中")
                sleep(5)
            elif self.scanner_handle.chack_page_source("下拉重新扫描") is True:
                logging.info("下拉重新扫描")
                self.scanner_handle.swipe_down()
                sleep(1)
                continue
            else:
                return False
