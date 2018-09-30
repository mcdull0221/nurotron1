__author__ = 'songxiaolin'
import xlrd
from xlutils.copy import copy
import sys, os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperaExcel:
    def __init__(self, file_path=None, i=None):
        if file_path is None:
            self.file_path = PATH("../config/case.xls")
        else:
            self.file_path = file_path
        if i is None:
            self.i = 0

        self.excel = self.get_excel()
        self.data = self.get_sheet(self.i)

    def get_excel(self):
        """
        获取excel
        :return:
        """
        excel = xlrd.open_workbook(self.file_path)
        return excel

    def get_sheet(self, i):
        """获取sheet"""
        table = self.excel.sheets()[i]
        return table

    def get_lines(self):
        """获取行数"""
        return self.data.nrows

    def get_cell(self, row, cell):
        """获取单元格"""
        data = self.data.cell(row, cell).value
        return data

    def write_value(self, row, value):
        read_vale = self.excel
        write_data = copy(read_vale)
        write_save = write_data.get_sheet(0)
        write_save.write(row, 9, value)
        write_data.save(self.file_path)


if __name__ == "__main__":
    opera = OperaExcel()
    print(opera.get_cell(1, 2))
    print(opera.write_value(6, 'pass'))
