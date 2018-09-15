import threading
from testSet.public.driver import BaseDriver
import time
import multiprocessing
from business.scanner_business import ScannerBusiness
from business.main_business import MainBusiness
from appium import webdriver
import HTMLTestRunner
import unittest
from util.server import Server
from util.write_user_command import WriteUserCommand


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super().__init__(methodName)
        global parames
        parames = parame


class testcase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpclass---->", str(parames))
        get_driver = BaseDriver()
        cls.driver = get_driver.android_driver(parames)

    def setUp(self):
        print('set up'+str(parames))
        pass

    def test_01(self):
        self.scanner_business = ScannerBusiness(self.driver)
        scanner_result = self.scanner_business.devices_found
        # print('test01'+str(parames))
        self.assertTrue(scanner_result)

    def test_02(self):
        print('this is test 2')
        self.main_business = MainBusiness(self.driver)
        map_change = self.main_business.map_change()
        self.assertIn('已选', map_change)

    def tearDown(self):
        print('tear down')

    @classmethod
    def tearDownClass(cls):
        print('tear down class')
        cls.driver.quit()


def appium_init():
    server = Server()
    server.main()


def get_suite(i):
    print("get_suite里的"+str(i))
    suite = unittest.TestSuite()
    suite.addTest(testcase('test_01', parame=i))
    suite.addTest(testcase('test_02', parame=i))
    # unittest.TextTestRunner().run(suite)
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    html_file = "E:/pythonProject/appiumTest/nurotron/result/report/" + now + "report"+str(i) +".html"
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
        print("i = " + str(i))
        # t = threading.Thread(target=get_suite, args=(i,)) 多线程启动
        t = multiprocessing.Process(target=get_suite, args=(i,))    # 多进程启动
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)

