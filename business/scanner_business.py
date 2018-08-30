__author__ = 'songxiaolin'
import logging
from Handle.scanner_handle import scannerHandle
from testSet.public.swipe import Swipe
from time import sleep


class scannerBusiness:
    def __init__(self, i):
        self.scanner_handle = scannerHandle(i)
        self.swipe = Swipe(i)

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
            # scannerHandle.chack_page_source("下拉重新扫描")
            if self.scanner_handle.chack_page_source("00:02:5B"):
                self.scanner_handle.click_driver()
                sleep(2)
                self.scanner_handle.click_driver_ok()
                return True
                break
            elif self.scanner_handle.chack_page_source("设备查找中"):
                print("设备查找中")
                pass
            elif self.scanner_handle.chack_page_source("下拉重新扫描"):
                print("下拉重新扫描")
                self.swipe.swipe_down()
                sleep(1)
                continue
            else:
                return False


