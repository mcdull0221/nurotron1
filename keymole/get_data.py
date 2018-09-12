__author__ = 'songxiaolin'
from util.opera_excle import OperaExcel


class GetData:
    def __init__(self):
        self.opera_excel = OperaExcel()

    def get_case_lines(self):
        """获取case的行数"""
        lines = self.opera_excel.get_lines()
        return lines

    def get_handle_step(self, row):
        """获取操作步骤里面的方法名字"""
        method_name = self.opera_excel.get_cell(row, 3)
        if method_name == '':
            return None
        return method_name

    def get_element_key(self, row):
        """获取操作元素的key"""
        element_key = self.opera_excel.get_cell(row, 4)
        if element_key == '':
            return None
        return element_key

    def get_handle_value(self, row):
        """获取操作值"""
        handle_value =  self.opera_excel.get_cell(row, 5)
        if handle_value == '':
            return None
        return handle_value

    def get_expect_element(self, row):
        """获取预期结果元素"""
        expect_element =  self.opera_excel.get_cell(row, 6)
        if expect_element == '':
            return None
        return expect_element

    def get_is_run(self, row):
        is_run = self.opera_excel.get_cell(row, 8)
        if is_run =="yes":
            return True
        else:
            return False

    def get_expect_handle(self, row):
        expect_step = self.opera_excel.get_cell(row,7)
        if expect_step == "":
            return None
        else:
            return expect_step


if __name__ == '__main__':
    get = GetData()
    print(get.get_element_key(6))
