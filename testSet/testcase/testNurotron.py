import random
import unittest
from time import sleep
import logging
import sys
sys.path.append('E:/pythonProject/appiumTest/nurotron')

from testSet.public.swipe import swipe
from testSet.public.driver import AppiumTest
from util.get_by_local import GetByLocal
from testSet.public.swipe import swipe


class Nurotrontest(unittest.TestCase):
    # def setUp(self):
    # 为了连续的执行测试用例，不用每个case都重载APP
    # 所以用setUpClass（cls） 于tearDownClass(cls)代替
    @classmethod
    def setUpClass(cls):
        cls.driver = AppiumTest().get_driver()
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    # def tearDown(self):
    #     self.driver.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_01_Connect(self):
        get_by_local = GetByLocal(self.driver)
        print("------------开始测试连接--------------")
        # 当未打开蓝牙时，会弹出对话框，点击确定
        try:
            # el1 = self.driver.find_element_by_id("android:id/button1")
            el1 = get_by_local.get_element('bleok')
            el1.click()
            sleep(2)
            # 会弹出警告弹框 app正在对手机进行定位
            em = get_by_local.get_element('locationOk')
            em.click()
            print("已确认对话框")
            # 会弹出警告弹框 app正在对手机进行定位
            sleep(1)
        except:
            logging.info('未发现蓝牙弹框')
            pass

        for i in range(1, 11):
            sleep(1)
            page = self.driver.page_source
            print("开始查找设备")
            if page.__contains__('设备查找中'):
                sleep(6)
                page1 = self.driver.page_source
                print("设备查找中")
                if page1.__contains__('00:02:5B'):
                    print("已找到设备")
                    el1 = get_by_local.get_element('driverList')
                    el1.click()
                    sleep(2)
                    el2 = get_by_local.get_element('connectSure')
                    el2.click()
                    sleep(2)
                    break
                elif i < 10:
                    print("未发现设备")
                    continue
                else:
                    logging.error('没有找到设备，请检查')
                    break
            elif page.__contains__('下拉重新扫描'):
                # self.driver.swipe(343, 329, 340, 700, 1000)
                print('下拉重新扫描')
                swipe.swipe_down()
                sleep(2)
                continue
        sleep(2)
        print('--------连接测试完成--------')
        activity = self.driver.current_activity
        self.assertEqual(".MainActivity", activity)

    def test_02_Map(self):
        sleep(5)
        print("---------进入主页面---------")
        mainPage = self.driver.page_source
        # print(mainPage)
        # 有可能会弹出无法连接设备的弹出框
        # 进入主页会弹出若希望使用Enduro拨打电话，请前往蓝牙设置界面进行配对并保存此设备 的对话框
        if mainPage.__contains__('设备无法连接'):
            # 如果弹出无法连接对话框点击确定
            self.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout'
                                              '/android.widget.FrameLayout/android.widget.LinearLayout/android.widget'
                                              '.ScrollView/android.widget.LinearLayout/android.widget.Button').click()
            logging.error('无法连接设备，请检查')
            sleep(2)
            try:
                # 弹框请前往配对，点击取消
                self.driver.find_element_by_xpath(
                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/and"
                    "roid.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Li"
                    "nearLayout/android.widget.Button[1]").click()
                sleep(2)
            except:
                pass
        elif mainPage.__contains__('若希望'):
            self.driver.find_element_by_xpath(
                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/and"
                "roid.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Li"
                "nearLayout/android.widget.Button[1]").click()
            sleep(2)
        else:
            pass

        # self.driver.background_app(2)
        # connected = self.get_Toast('设备已连接')
        # print(connected)

        map1 = self.driver.find_element_by_id("com.nurotron.ble_ui:id/program1")
        sleep(3)
        if map1.text.__contains__('已选'):
            map2 = self.driver.find_element_by_id("com.nurotron.ble_ui:id/program2")
            map2.click()
            sleep(2)
            self.assertIn('已选', map2.text)
            print('切换为程序二成功')
        else:
            map1.click()
            sleep(2)
            map1 = self.driver.find_element_by_id("com.nurotron.ble_ui:id/program1")
            self.assertIn('已选', map1.text)
            print('切换为程序一成功')

    def test_03_Vol(self):
        sleep(1)
        print('---------开始测试音量-----------')
        # vol = self.driver.find_element_by_id('com.nurotron.ble_ui:id/vol')
        # print('当前音量为：'+ vol.text)
        for i in range(1, 13):
            self.driver.find_element_by_id('com.nurotron.ble_ui:id/add_vol').click()
            sleep(1)
        vol = self.driver.find_element_by_id('com.nurotron.ble_ui:id/vol')
        self.assertEqual('12', vol.text)
        sleep(1)

        for i in range(1, 14):
            self.driver.find_element_by_id('com.nurotron.ble_ui:id/mute').click()
            sleep(1)
        vol = self.driver.find_element_by_id('com.nurotron.ble_ui:id/vol')
        self.assertEqual('1', vol.text)
        print('测试完成')

    def test_04_MapName(self):
        print('-------开始测试程序名称------')
        sleep(1)
        self.driver.swipe(600, 1100, 100, 1100, 500)
        # swipe_on('left')
        sleep(1)
        edittext = self.driver.find_element_by_id('com.nurotron.ble_ui:id/programText')
        edittext.clear()    # 清除输入的内容
        # 从预选里 随机选取10个字符
        name = random.sample('zxcvbnm,./asdfghjkl;qwertyuiop[]1234567890一二三四五六七八九十', 10)
        '''
        name 里面输出的是一个list
        要转化为字符串才能和map名称对比,使用下面的方法
        str = ''
        str.join(name)
        '''
        str = ''
        str = str.join(name)+' 已选'
        str = str.upper()
        edittext.send_keys(name)
        sleep(1)
        self.driver.swipe(100, 1100, 600, 1100, 500)
        sleep(2)
        # page = self.driver.page_source
        map1 = self.driver.find_element_by_id("com.nurotron.ble_ui:id/program1")
        if map1.text.__contains__('已选'):
            self.assertEqual(str, map1.text)
        else:
            map2 = self.driver.find_element_by_id("com.nurotron.ble_ui:id/program2")
            self.assertEqual(str, map2.text)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 将测试用例加入到容器中
    suite.addTest(Nurotrontest('test_01_Connect'))
    suite.addTest(Nurotrontest('test_02_Map'))
    suite.addTest(Nurotrontest('test_03_Vol'))
    suite.addTest(Nurotrontest('test_04_MapName'))
    unittest.TextTestRunner(verbosity=4).run(suite)

