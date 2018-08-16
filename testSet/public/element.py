__author__ = 'songxiaolin'
from testSet.public.driver import AppiumTest


class Element:
    """
    封装Appium中关于元素对象的方法
    """
    def __init__(self):
        at = AppiumTest()
        self.driver = at.get_driver()

    def get_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    def get_name(self, name):
        element = self.driver.find_element_by_name(name)
        return element

    def over(self):
        element = self.driver.quit()
        return element

    def back(self):
        self.driver.keyevent(4)

    def get_classes(self, classesname):
        elements = self.driver.find_elements_by_class_name(classesname)
        return elements

    def get_ids(self, ids):
        elements = self.driver.find_elements_by_id(ids)
        return elements
