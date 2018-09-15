__author__ = 'songxiaolin'
from util.read_init import ReadIni


class GetByLocal:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key, section=None):
        read_ini = ReadIni()
        local = read_ini.get_value(key, section)
        if local != None:
            # split()通过指定分隔符对字符串进行切片
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            if by == 'id':
                return self.driver.find_element_by_id(local_by)
            elif by == 'className':
                return self.driver.find_element_by_class_name(local_by)
            else:
                return self.driver.find_element_by_xpath(local_by)
        else:
            return None


