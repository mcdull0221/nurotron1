__author__ = 'songxiaolin'
from testSet.public.driver import BaseDriver


class Driver:
    def driver(self, i):
        base_driver = BaseDriver()
        driver = base_driver.android_driver(i)
        return driver
