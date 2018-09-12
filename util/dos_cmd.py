__author__ = 'songxiaolin'
import os

# print(os.system('adb devices')) # 无法收集结果
# print(os.popen('adb devices').readlines()) # 收集的结果是list
class DosCmd:
    def excute_cmd_result(self, command):
        result_list = []
        result = os.popen(command).readlines()
        for i in result:
            if i == '\n':
                continue
            result_list.append(i.strip('\n'))
        return result_list

    def excute_cmd(self, command):
        os.system(command)

if __name__ == '__main__':
    dos = DosCmd()
    print(dos.excute_cmd_result('adb devices'))
    # r = dos.excute_cmd_result('adb shell pm list packages')
    # print(r)
    # i = 'package:com.nurotron.ble_ui'
    # if i in r:
    #     print('yes')
    # else:
    #     print('no')
