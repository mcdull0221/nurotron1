import sys
import os
curpath = os.path.abspath(os.path.dirname(__file__))
rootpath = os.path.split(curpath)[0]
sys.path.append(rootpath)
from keymole.get_data import GetData
from keymole.action_method import ActionMethod
from util.server import Server


class RunMain:
    def run_method(self):
        server = Server()
        server.main()
        data = GetData()
        action_method = ActionMethod()
        lines = data.get_case_lines()
        for i in range(1, lines):
            handle_step = data.get_handle_step(i)
            element_key = data.get_element_key(i)
            handle_value = data.get_handle_value(i)
            expect_key = data.get_expect_element(i)
            expect_step = data.get_expect_handle(i)

            excute_method = getattr(action_method, handle_step)     # excute_method是一个对象，加括号才被执行
            if element_key is not None:
                excute_method(element_key, handle_value)
            else:
                excute_method(handle_value)
            if expect_step is not None:
                expect_result = getattr(action_method, expect_step)
                result = expect_result(expect_key)
                if result:
                    data.write_value(i, "PASS")
                else:
                    data.write_value(i, "FAIL")



if __name__ == '__main__':
    run = RunMain()
    run.run_method()
