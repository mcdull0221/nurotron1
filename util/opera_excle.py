__author__ = 'songxiaolin'
import xlrd
import sys, os
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class OperaExcel:
    def __init__(self, file_path=None, i=None):
        if file_path is None:
            self.file_path = PATH("../config/case.xlsx")
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


if __name__ == "__main__":
    opera = OperaExcel()
    print(opera.get_cell(1, 2))
