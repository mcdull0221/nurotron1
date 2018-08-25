__author__ = 'songxiaolin'
from util.dos_cmd import DosCmd
from util.port import Port
import threading
from util.write_user_command import WriteUserCommand
class Server:
    def __init__(self):
        self.dos = DosCmd()
        self.write_file = WriteUserCommand()
        self.device_list = self.get_devices()

    def get_devices(self):
        """
        通过命令行 获取设备信息
        返回一个列表
        """
        devices_list = []
        result_list = self.dos.excute_cmd_result('adb devices')
        if len(result_list) >= 2:
            for i in result_list:
                if "List" in i:
                    continue
                devices_info = i.split('\t')
                if devices_info[1] == 'device':
                    devices_list.append(devices_info[0])
            return devices_list
        else:
            return None

    def create_port_list(self,start_port):
        """
        创建可用端口
        :return:
        """
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.device_list)
        return port_list

    def create_command_list(self, i):
        """
        appium -p 4700 -bp 4701 -U *** --no-reset --session-override
        :return:command_list
        """
        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        device_list = self.device_list
        # for i in range(len(device_list)):
        commend = "appium -p "+str(appium_port_list[i])+" -bp "+str(bootstrap_port_list[i])+" -U "+device_list[i]+\
                  " --no-reset --session-override"
        command_list.append(commend)
        #调用write_data方法将参数写人yaml文件中
        self.write_file.write_data(i, device_list[i], bootstrap_port_list[i], appium_port_list[i])
        return command_list

    def start_server(self, i):
        """
        命令行启动服务
        当有多个设备时，多线程启动
        :return:
        """
        self.start_list = self.create_command_list(i)
        self.dos.excute_cmd(self.start_list[0])
        # self.dos.excute_cmd(self.start_list[i])
        # 启动多个线程时，用i会报错，因为start_list里面只有一个元素。

    def kill_server(self):
        '''
        cmd查找有无进程 tasklist | find "***.exe"
        cmd终止程序 taskkill | -F -PID ***.exe
        :return:
        '''
        server_list = self.dos.excute_cmd_result('tasklist | find "node.exe"')
        if len(server_list) > 0:
            self.dos.excute_cmd('taskkill | -F -PID node.exe')

    def main(self):
        """
        多线程启动appium服务
        先杀掉多余进程和情况yaml文件
        :return:
        """
        self.write_file.clear_data()
        self.kill_server()
        for i in range(len(self.device_list)):
            appium_start = threading.Thread(target=self.start_server, args=(i,))
            appium_start.start()


if __name__ == '__main__':
    server = Server()
    # print(server.get_devices())
    # print(server.create_command_list())
    print(server.main())
