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
        return tamp