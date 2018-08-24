import threading
import time
from business.scanner_business import scannerBusiness
from appium import webdriver
import HTMLTestRunner
import unittest

class testcase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.scanner_business = scannerBusiness()

    def setUp(self):
        print('set up')

    def tearDown(self):
        print('tear down')

    @classmethod
    def tearDownClass(cls):
        print('tear down class')

    def test_01(self):
        print('test01')

    def test_02(self):
        print('test02')

def get_suite(i):
    suite = unittest.TestSuite()
    suite.addTest(testcase('test_02'))
    suite.addTest(testcase('test_01'))
    # unittest.TextTestRunner().run(suite)
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    html_file = "E:/pythonProject/appiumTest/nurotron/result/report/" + now + "report"+str(i) +".html"
    fp = open(html_file, "wb")
    HTMLTestRunner.HTMLTestRunner(stream=fp, title='APP测试报告', description='用例执行情况').run(suite)
    fp.close()

if __name__ =='__main__':
    # unittest.main()
    # 多线程
    threads = []
    for i in range(2):
        # print i
        t = threading.Thread(target=get_suite, args=(i,))
        threads.append(t)
    for j in threads:
        j.start()

