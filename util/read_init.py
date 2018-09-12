__author__ = 'songxiaolin'
import configparser

'''
read_ini = configparser.ConfigParser()
read_ini.read('E:/pythonProject/appiumTest/nurotron/config/localElement.ini')
# data = read_ini.read('E:/pythonProject/appiumTest/nurotron/config/localElement.ini')
# print(data)  不能赋值给data，data是一个list，read_ini才是对象
print(read_ini.get('connect_element','username'))
'''

class ReadIni():
    def __init__(self,file_path= None):
        if file_path == None:
            self.file_path = 'E:/pythonProject/appiumTest/nurotron/config/localElement.ini'
        else:
            self.file_path =file_path
        self.data = self.read_ini()

    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        # data = read_ini.read(self.file_path)  data将只是file_path的路径，读取到的内容还在read_ini里。
        return read_ini

    def get_value(self, key, section=None):
        if section == None:
            section = 'connect_element'
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value

if __name__ == '__main__':
    read_ini = ReadIni()


