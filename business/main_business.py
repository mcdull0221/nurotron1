__author__ = 'songxiaolin'
import logging
from Handle.main_handle import MainHandle
from time import sleep


class MainBusiness:
    def __init__(self, i):
        self.main_handle = MainHandle(i)

    def click_pairing_no(self):
        try:
            sleep(2)
            self.main_handle.click_pairing_no()
            sleep(2)
        except:
            print('未发现蓝牙配对弹出框')
            pass

    def map_change(self):
        map1 = self.main_handle.get_map1()
        if map1.text.__contains__('已选'):
            self.main_handle.click_map2()
            sleep(1)
            map2 = self.main_handle.get_map2()
            self.assertIn('已选', map2.text)
        else:
            pass
