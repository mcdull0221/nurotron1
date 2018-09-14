__author__ = 'songxiaolin'
from page.main_page import MainPage


class MainHandle:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)

    def click_pairing_no(self):
        """点击 取消蓝牙配对弹框"""
        self.main_page.pairing_no().click()

    def get_map1(self):
        return self.main_page.map1()

    def get_map2(self):
        return self.main_page.map2()

    def get_map3(self):
        return self.main_page.map3()

    def get_map4(self):
        return self.main_page.map4()

    def click_map1(self):
        """点击 map1"""
        self.main_page.map1().click()

    def click_map2(self):
        """点击 map2"""
        self.main_page.map2().click()

    def click_map3(self):
        """点击 map1"""
        self.main_page.map3().click()

    def click_map4(self):
        """点击 map1"""
        self.main_page.map4().click()

    def get_volume(self):
        """返回当前音量"""
        return self.main_page.volume()

    def click_volume_sub(self):
        """点击 音量减"""
        self.main_page.volume_sub().click()

    def click_volume_add(self):
        """点击 map1"""
        self.main_page.volume_add().click()

    def click_action_icon(self):
        """点击 左上角菜单栏"""
        self.main_page.action_icon().click()

    def send_map_name(self, name):
        """发送程序名称"""
        self.main_page.map_name().send_keys(name)

    def click_mode_rich(self):
        """点击 丰富模式"""
        self.main_page.mode_rich().click()

    def click_mode_normal(self):
        """点击 日常模式"""
        self.main_page.mode_normal().click()

    def click_mic_or_aux(self):
        """点击 mic/aux"""
        self.main_page.mic_or_aux().click()

    def click_mic_and_aux(self):
        """点击 mic+aux"""
        self.main_page.mic_and_aux().click()

    def click_mic_and_tcoil(self):
        """点击 mic+tcoil"""
        self.main_page.mic_and_tcoil().click()

    def click_blue(self):
        """点击 蓝牙模式"""
        self.main_page.blue().click()

    def click_ctone_on(self):
        """点击 易懂开"""
        self.main_page.ctone_on().click()

    def click_ctone_off(self):
        """点击 易懂关"""
        self.main_page.ctone_off().click()

    def click_noise_on(self):
        """点击 降噪开"""
        self.main_page.noise_on().click()

    def click_input_ratio2(self):
        """点击 输入比1:2"""
        self.main_page.input_ratio2().click()

    def click_input_ratio3(self):
        """点击 输入比1:3"""
        self.main_page.menu().click()

    def click_input_ratio5(self):
        """点击 输入比1:5"""
        self.main_page.input_ratio5().click()

    def click_input_ratio9(self):
        """点击 输入比1:9"""
        self.main_page.input_ratio9().click()

    def click_menu(self):
        """点击 点击侧边栏的主菜单"""
        self.main_page.menu().click()

    def click_setting(self):
        """点击 点击侧边栏的定位"""
        self.main_page.setting().click()

    def click_state(self):
        """点击 点击侧边栏的定位"""
        self.main_page.state().click()

    def click_location(self):
        """点击 点击侧边栏的定位"""
        self.main_page.location().click()

    def click_log(self):
        """点击 点击侧边栏的日志"""
        self.main_page.log().click()

    def click_about(self):
        """点击 侧边栏的关于"""
        self.main_page.about().click()

    def swipe_left(self):
        self.main_page.swipe_left()

    def swipe_right(self):
        self.main_page.swipe_right()
