import threading
import time
from business.scanner_business import scannerBusiness
from appium import webdriver
import HTMLTestRunner
import unittest
from util.server import Server


class ParameTestCase(unittest.TestCase):
    def __init__(self, methodName='runTest', parame=None):
        super(ParameTestCase, self).__init__(methodName)
        global parames
        parames = parame


class testcase(ParameTestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass'+ str(parames))
        # cls.scanner_business = scannerBusiness(i)

    def setUp(self):
        print('set up'+str(parames))

    def tearDown(self):
        print('tear down')

    @classmethod
    def tearDownClass(cls):
        print('tear down class')

    def test_01(self):
        self.scanner_business = scannerBusiness(i)
        print('test01'+str(parames))

    def test_02(self):
        print('test02'+ str(parames))

def appium_init():
    server = Server()
    server.main()

def get_suite(i):
    print("get_suite里的"+str(i))
    suite = unittest.TestSuite()
    suite.addTest(testcase('test_02', parame=i))
    # suite.addTest(testcase('test_01'))
    suite.addTest(testcase('test_01', parame=i))
    unittest.TextTestRunner().run(suite)
    # now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    # html_file = "E:/pythonProject/appiumTest/nurotron/result/report/" + now + "report"+str(i) +".html"
    # fp = open(html_file, "wb")
    # HTMLTestRunner.HTMLTestRunner(stream=fp, title='APP测试报告', description='用例执行情况').run(suite)
    # fp.close()


if __name__ == '__main__':
    # unittest.main()
    # 多线程
    appium_init()
    threads = []
    for i in range(1):
        print("i = " + str(i))
        t = threading.Thread(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()
        time.sleep(1)

