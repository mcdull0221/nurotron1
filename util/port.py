__author__ = 'songxiaolin'
from util.dos_cmd import DosCmd
class Port:
    '''
    检查端口是否被暂用
    netstat -ano | findstr ****
    有结果即有占用
    '''
    def port_is_used(self, port):
        flag = None
        self.dos = DosCmd()
        result = self.dos.excute_cmd_result('netstat -ano | findstr '+ str(port))
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, device_list):
        '''
        生成可用端口
        :param start_port: 起始端口
        :param device_list: 获取到的设备数
        :return:根据设备数返回一个可用端口的列表
        '''
        port_list =[]
        if device_list != None:
            while len(port_list) != len(device_list):
                if self.port_is_used(start_port) != True:
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            return None
            print("生成可用端口失败")


if __name__ == '__main__':
    port = Port()
    print(port.port_is_used(4723))
    print(port.create_port_list(4722, [1,2,3]))

