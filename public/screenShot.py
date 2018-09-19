__author__ = 'songxiaolin'
import time


class screenShot():
    # 截图功能
    def getScreenShot(self):
        time = self.getTime()
        filename = '../jpg/%s.png' % time
        self.driver.get_screenshot_as_file(filename)

    # 获取时间戳
    def getTime(self):
        tamp = int(time.time())
        now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
        return now


if __name__ == '__main__':
    screen_shot = screenShot()
    now = screen_shot.getTime()
    print(now)
