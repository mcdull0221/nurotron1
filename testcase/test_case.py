import sys
import os
from public.driver import BaseDriver
import time
import multiprocessing
from business.scanner_business import ScannerBusiness
from business.main_business import MainBusiness
from business.login_business import LoginBusiness
import HTMLTestRunner
import unittest
from util.server import Server
from util.write_user_command import WriteUserCommand
curpath = os.path.abspath(os.path.dirname(__file__))
rootpath = os.path.split(curpath)[0]
sys.path.append(rootpath)
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super().__init__(methodName)
        global parames
        parames = parame


class testcase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        # print("setUpclass---->", str(parames))
        get_driver = BaseDriver()
        cls.driver = get_driver.android_driver(parames)
        cls.scanner_business = ScannerBusiness(cls.driver)
        cls.main_business = MainBusiness(cls.driver)
        cls.login_business = LoginBusiness(cls.driver)

    def setUp(self):
        # print('set up'+str(parames))
        pass

    def test_login_00(self):
        login_fail = self.login_business.login_user_error()
        login_success = self.login_business.login_success()
        self.assertNotEqual(login_fail, login_success)

    def test_connect_01(self):
        # self.scanner_business = ScannerBusiness(self.driver)
        scanner_result = self.scanner_business.devices_found
        self.assertTrue(scanner_result)

    def test_changemap_02(self):
        # self.main_business = MainBusiness(self.driver)
        map_change = self.main_business.map_change()
        self.assertTrue(map_change)

    def test_vol_add_03(self):
        vol_add = self.main_business.vol_add()
        self.assertEqual(12, vol_add)

    def test_vol_sub_04(self):
        vol_sub = self.main_business.vol_sub()
        self.assertEqual(1, vol_sub)

    def tearDown(self):
        # print('tear down')
        # 捕获异常，失败时截图
        if sys.exc_info()[0]:
            # self.driver.save_screenshot(PATH('../result/screenshot/screenshot01.png'))
            now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
            png_file = PATH("../result/screenshots/") + "\\" + now + "driver" + str(parames) + ".png"
            self.driver.save_screenshot(png_file)

    @classmethod
    def tearDownClass(cls):
        print('tear down class')
        cls.driver.quit()


def appium_init():
    server = Server()
    server.main()


def stop_appium():
    server = Server()
    server.kill_server()


def get_suite(i):
    print("get_suite里的"+str(i))
    suite = unittest.TestSuite()
    suite.addTest(testcase('test_login_00', parame=i))
    suite.addTest(testcase('test_connect_01', parame=i))
    suite.addTest(testcase('test_changemap_02', parame=i))
    suite.addTest(testcase('test_vol_add_03', parame=i))
    suite.addTest(testcase('test_vol_sub_04', parame=i))
    # unittest.TextTestRunner().run(suite)
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    html_file = PATH("../result/report/") + "\\" + now + "report"+str(i) + ".html"
    fp = open(html_file, "wb")
    HTMLTestRunner.HTMLTestRunner(stream=fp, title='APP测试报告', description='用例执行情况').run(suite)
    fp.close()


def get_count():
    write_user_file = WriteUserCommand()
    count = write_user_file.get_file_lines()
    return count


if __name__ == '__main__':
    # unittest.main()
    # 多线程
    appium_init()
    threads = []
    for i in range(get_count()):
        # print("i = " + str(i))
        # t = threading.Thread(target=get_suite, args=(i,)) 多线程启动
        t = multiprocessing.Process(target=get_suite, args=(i,))    # 多进程启动
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)
    stop_appium()
