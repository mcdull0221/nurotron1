__author__ = 'songxiaolin'
import logging
from Handle.main_handle import MainHandle
from time import sleep


class MainBusiness:
    def __init__(self, driver):
        self.driver = driver
        self.main_handle = MainHandle(self.driver)

    def click_pairing_no(self):
        try:
            sleep(2)
            self.main_handle.click_pairing_no()
            sleep(2)
        except:
            print('未发现蓝牙配对弹出框')
            pass

    def map_change(self):
        self.click_pairing_no()
        sleep(2)
        # map1 = self.main_handle.get_map1()
        # if map1.text.__contains__('已选'):
        #     self.main_handle.click_map2()
        #     sleep(1)
        #     map2 = self.main_handle.get_map2()
        #     return map2.text
        # else:
        #     self.main_handle.click_map1()
        #     map1 = self.main_handle.get_map1()
        #     return map1.text
        map1_sel = self.main_handle.get_map1().is_selected()
        if map1_sel is True:
            self.main_handle.click_map2()
            sleep(1)
            map2_sel = self.main_handle.get_map2().is_selected()
            return map2_sel
        else:
            self.main_handle.click_map1()
            map1_sel = self.main_handle.get_map1().is_selected()
            return map1_sel
