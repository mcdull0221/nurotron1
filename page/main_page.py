__author__ = 'songxiaolin'
from page.base_page import BasePage
from util.get_by_local import GetByLocal


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.base_page = BasePage(self.driver)
        # self.driver = self.base_page.driver
        self.get_by_local = GetByLocal(self.driver)

    def get_element(self, key, section='mainpage_element'):
        return self.get_by_local.get_element(key, section)

    def pairing_no(self):
        return self.get_element('pairingNO')

    def map1(self):
        return self.get_element('map1')

    def map2(self):
        return self.get_element('map2')

    def map3(self):
        return self.get_element('map3')

    def map4(self):
        return self.get_element('map4')

    def volume(self):
        return self.get_element('volume')

    def volume_sub(self):
        return self.get_element('volumeSub')

    def volume_add(self):
        return self.get_element('volumeAdd')

    def action_icon(self):
        return self.get_element('actionIcon')

    def map_name(self):
        return self.get_element('mapName')

    def mode_rich(self):
        return self.get_element('modeRich')

    def mode_normal(self):
        return self.get_element('modeNormal')

    def mic_or_aux(self):
        return self.get_element('mic/aux')

    def mic_and_aux(self):
        return self.get_element('mic+aux')

    def mic_and_tcoil(self):
        return self.get_element('mic+tcoil')

    def blue(self):
        return self.get_element('blue')

    def ctone_on(self):
        return self.get_element('ctoneON')

    def ctone_off(self):
        return self.get_element('ctoneOFF')

    def noise_on(self):
        return self.get_element('noiseON')

    def noise_off(self):
        return self.get_element('noiseOFF')

    def input_ratio2(self):
        return self.get_element('inputratio2')

    def input_ratio3(self):
        return self.get_element('inputratio3')

    def input_ratio5(self):
        return self.get_element('inputratio5')

    def input_ratio9(self):
        return self.get_element('inputratio9')

    def menu(self):
        return self.get_element('menu')

    def setting(self):
        return self.get_element('setting')

    def state(self):
        return self.get_element('state')

    def location(self):
        return self.get_element('location')

    def log(self):
        return self.get_element('log')

    def about(self):
        return self.get_element('about')

    def autoswitch(self):
        return self.get_element('autoswitch')

    def sceneON(self):
        return self.get_element('sceneON')

    def sceneOFF(self):
        return self.get_element('sceneOFF')

    def get_page_source(self):
        """获取页面所有元素"""
        page_source = self.base_page.get_page_source()
        return page_source

    def swipe_left(self):
        self.base_page.swipe_left()

    def swipe_right(self):
        self.base_page.swipe_right()


