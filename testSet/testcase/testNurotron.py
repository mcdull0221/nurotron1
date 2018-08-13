# coding=utf-8
import random
import unittest
from functools import wraps
from time import sleep
import time
from appium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import HTMLTestRunner
from testSet.public import getToast
from testSet.public import screenShot


class Nurotrontest(unittest.TestCase):
    # def setUp(self):
    # 为了连续的执行测试用例，不用每个case都重载APP
    # 所以用setUpClass（cls） 于tearDownClass(cls)代替
    @classmethod
    def setUpClass(cls):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '7.1.2',
            'deviceName': '298384e47d74',
            # 用activity启动报错，所以用app启动
            'app': 'E:\\app-debug.apk',
            'udid': '298384e47d74',
            'notReset': 'true',
            # 自动确定确定应用权限
            'autoGrantPermissions': 'true',
            'unicodeKeyboard': 'true',
            'resetKeyboard': 'true',
            'automationName': 'Uiautomator2'
        }

        # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    # def tearDown(self):
    #     self.driver.quit()


    # 获取页面toast
    def _find_toast(message, timeout, poll_frequency, driver):
        message = '//*[@text=\'{}\']'.format(message)
        element = WebDriverWait(driver, timeout, poll_frequency).until(
            expected_conditions.presence_of_element_located((By.XPATH, message)))
        return element
        # self._find_toast('Hello selendroid toast!',10,0.5,self.driver) 来调用

    def get_Toast(self, message):  # 查找toast值
        '''
        method explain:查找toast的值,与find_Toast实现方法一样，只是不同的2种写法
        parameter explain：【text】查找的toast值
        Usage:
            device.get_Toast('再按一次退出iBer')
        '''
        logging.info("查找toast值---'%s'" % (message))
        try:
            message = '//*[@text=\'{}\']'.format(message)
            ele = WebDriverWait(self.driver, 5, 0.5).until(
                expected_conditions.presence_of_element_located((By.XPATH, message)))
            return ele.get_attribute("text")
            logging.info("查找到toast----%s" % message)
        except:
            logging.error("未查找到toast----%s" % message)
            return False

    def test_01_Connect(self):
        print("------------开始测试连接--------------")

        # 当未打开蓝牙时，会弹出对话框，点击确定
        try:
            el1 = self.driver.find_element_by_id("android:id/button1")
            el1.click()
            sleep(2)
            # 会弹出警告弹框 app正在对手机进行定位
            em = self.driver.find_element_by_xpath(
                '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout'
                '/android.widget.FrameLayout/android.widget.LinearLayout/android'
                '.widget.LinearLayout/android.widget.LinearLayout/android.widget'
                '.Button[2]')
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
                    el1 = self.driver.find_element_by_xpath(
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                        "/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ListView/android.widget"
                        ".LinearLayout")
                    el1.click()
                    sleep(2)
                    el2 = self.driver.find_element_by_id("android:id/button1")
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
                self.driver.swipe(343, 329, 340, 700, 1000)
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
    unittest.TextTestRunner(verbosity=(4)).run(suite)
    # 获取当前时间
    # timestr = time.strtime('%Y-%m-%d %X', time.localtime(time.time()))
    # filename = r"E:\\testReport\\" + timestr + '.html'  # 存放报告的路径
    # f = open(filename, 'wb')  # 结果写入文件
    # # 配置参数，输出报告路径，报告标题，描述
    # runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='Report_title', description='Report_description',
    #                                        verbosity=2)
    # runner.run(suite)
    # # result = runner.run(suite)
    # # result.success_count # 运行成功的数目
    # # result.testsRun   # 运行测试用例的数目
    # # result.failfast   # 运行失败的数目
    # f.close()
