import sys
import os
curpath = os.path.abspath(os.path.dirname(__file__))
rootpath = os.path.split(curpath)[0]
sys.path.append(rootpath)
from keymole.get_data import GetData
from keymole.action_method import ActionMethod
from util.server import Server
from public.driver import BaseDriver


class RunMain:
    def __init__(self):
        self.server = Server()
        self.server.main()
        base_driver = BaseDriver()
        self.driver = base_driver.android_driver(0)
        self.data = GetData()
        self.lines = self.data.get_case_lines()

    def operate_page(self, i):
        operate_page = self.data.get_operate_page(i)
        action_method = ActionMethod(operate_page, self.driver)
        return action_method

    def run_method(self):
        for i in range(1, self.lines):
            operate_page = self.operate_page(i)
            handle_step = self.data.get_handle_step(i)
            element_key = self.data.get_element_key(i)
            handle_value = self.data.get_handle_value(i)
            expect_element = self.data.get_expect_element(i)
            expect_step = self.data.get_expect_handle(i)

            excute_method = getattr(operate_page, handle_step)     # excute_method是一个对象，加括号才被执行
            if element_key is not None:
                excute_method(element_key, handle_value)
            else:
                excute_method(handle_value)
            if expect_step is not None:
                expect_result = getattr(operate_page, expect_step)
                result = expect_result(expect_element)
                if result is not None:
                    self.data.write_value(i, "PASS")
                else:
                    self.data.write_value(i, "FAIL")


if __name__ == '__main__':
    run = RunMain()
    run.run_method()
