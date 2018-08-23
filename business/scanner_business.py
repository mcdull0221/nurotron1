import logging

__author__ = 'songxiaolin'
from Handle.scanner_handle import scannerHandle
from testSet.public.swipe import swipe
from time import sleep

class scannerBusiness:
    def __init__(self):
        self.scanner_handle = scannerHandle()

    def connect_devices(self):
        try:
            self.scanner_handle.click_ble_ok()
            sleep(2)
            self.scanner_handle.click_location_ok()
            sleep(2)
        except:
            logging.info('未发现蓝牙弹框')
            pass

    def get_scanner_page(self):
        scannerpage = self.driver.page_source
        return scannerpage

    def devices_nofound(self):
        self.connect_devices()
        # for i in range(1, 11):
        #     sleep(1)
        #     page = self.driver.page_source
        #     if page.__contains__('设备查找中'):
        #         sleep(6)
        #         page1 = self.driver.page_source
        #         if page1.__contains__('00:02:5B'):
        #             self.scanner_handle.click_driver()
        #             sleep(2)
        #             self.scanner_handle.click_driver_ok()
        #             return True
        #             break
        #         elif i < 10:
        #             print("未发现设备")
        #             continue
        #         else:
        #             logging.error('没有找到设备，请检查')
        #             break
        #     elif page.__contains__('下拉重新扫描'):
        #         # self.driver.swipe(343, 329, 340, 700, 1000)
        #         print('下拉重新扫描')
        #         swipe.swipe_down()
        #         sleep(2)
        #         continue

        for i in range(1, 11):
            sleep(10)
            scanner_page = self.get_scanner_page()
            if scanner_page.__contains__('00:02:5B'):
                self.scanner_handle.click_driver()
                sleep(2)
                self.scanner_handle.click_driver_ok()
                return True
                break
            elif scanner_page.__contains__('设备查找中'):
                pass
            elif scanner_page.__contains__('下拉重新扫描'):
                swipe.swipe_down()
                sleep(1)
                continue
            else:
                return False

