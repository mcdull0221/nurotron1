# coding=utf-8
from keymole.get_data import GetData
from keymole.action_method import ActionMethod


class RunMain:
    def __init__(self):
        self.data = GetData()
        # self.action_method = ActionMethod()

    def run_method(self):
        lines = self.data.get_case_lines()
        for i in range(1, lines):
            print(i)


if __name__ == '__main__':
    run = RunMain()
    run.run_method()
