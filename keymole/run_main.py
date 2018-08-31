# coding=utf-8
from keymole.get_data import GetData
from keymole.action_method import ActionMethod


class RunMain:
    def __init__(self):
        self.data = GetData()
        self.action_method = ActionMethod()

    def run_method(self):
        lines = self.data.get_case_lines()
        for i in range(1, lines):
            handle_step = self.data.get_handle_step(i)
            element_key = self.data.get_element_key(i)
            handle_value = self.data.get_handle_value(i)
            expect_element = self.data.get_expect_element(i)
            excute_method = getattr(self.action_method, handle_step)
            if handle_value != None:
                excute_method(element_key, handle_value)
            else:
                excute_method(element_key)
            if expect_element != None:
                result_method = getattr(self.action_method, expect_element)
                result_method()


if __name__ == '__main__':
    run = RunMain()
    run.run_method()
