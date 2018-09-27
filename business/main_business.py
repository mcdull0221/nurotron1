import random

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

    def vol_add(self):
        vol = self.main_handle.get_volume().text
        print('当前音量：'+vol)
        if vol is None:
            logging.error('未发现音量')
            return
        else:
            for i in range(int(vol), 14):
                self.main_handle.click_volume_add()
                sleep(1)
        vol_now = self.main_handle.get_volume().text
        return int(vol_now)

    def vol_sub(self):
        vol = self.main_handle.get_volume().text
        if vol is None:
            logging.error('未发现音量')
            return
        else:
            for i in range(1, 14):
                self.main_handle.click_volume_sub()
                sleep(1)
        vol_now = self.main_handle.get_volume().text
        return int(vol_now)

    def change_map_name(self):
        # 从预选里 随机选取10个字符
        name = random.sample('zxcvbnm,./asdfghjkl;qwertyuiop[]1234567890一二三四五六七八九十', 10)
        '''
                name 里面输出的是一个list
                要转化为字符串才能和map名称对比,使用下面的方法
                str = ''
                str.join(name)
         '''
        str = ''
        map_name = str.join(name)
        print(map_name)
        self.main_handle.send_map_name(map_name)
        sleep(1)
        self.main_handle.swipe_left()


if __name__ == '__main__':
    main_business = MainBusiness(0)
    main_business.change_map_name()
