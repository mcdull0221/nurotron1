__author__ = 'songxiaolin'
import yaml


class WriteUserCommand:
    def read_data(self):
        '''加载yaml数据'''
        with open("../config/userConfig.yaml") as fr:
            data = yaml.load(fr)
            # print(data['user_info_0']['bp'])
            return data

    def get_value(self, key, port):
         """
         获取value
         :param key: yaml中user_info编号,相当于第几个手机
         :param port: 数组中的key值
         :return:value
         """
         data = self.read_data()
         value = data[key][port]
         return value

    def write_data(self, i,device, bp, port):
        '''
        写入数据
        '''
        data = self.join_data(i,device, bp, port)
        with open("../config/userConfig.yaml", 'a') as fr:
            yaml.dump(data, fr)

    def join_data(self, i,device, bp, port):
        '''
        拼接数据
        '''
        data = {
            "user_info_"+str(i): {
                "deviceName":device,
                "bp":bp,
                "port": port
            }
        }
        return data

    def clear_data(self):
        with open("../config/userConfig.yaml", 'w') as fr:
            fr.truncate()
            # fileObject.truncate( [ size ]) 则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。
        fr.close()


if __name__ == "__main__":
    write_file = WriteUserCommand()
    print(write_file.get_value('user_info_2', 'port'))
