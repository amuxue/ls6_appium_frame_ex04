# 点击通讯录
from appium.webdriver.common.mobileby import MobileBy


from frame.base_page import BasePage
from page.market_page import MarketPage


class MainPage(BasePage):
    def goto_market_page(self):
        self.run_steps("../page/main_page.yaml","goto_market_page")
        return MarketPage(self.driver)