# 启动app、关闭app、重启app、进入首页。。。
from appium import webdriver

from frame.base_page import BasePage
from page.main_page import MainPage


class App(BasePage):
    def start(self):
        if self.driver==None:
            caps={}
            caps = {}
            caps["platformName"] = "android"
            caps["appPackage"] = "com.xueqiu.android"
            caps["deviceName"] = "emulator-5554"
            caps["appActivity"] = ".view.WelcomeActivityAlias"
            caps["noReset"] = "true"
            caps["ensureWebviewsHavePages"] = True
            # 设置页面等待空闲状态的时间为0秒
            caps['settings[waitForIdleTimeout]'] = 1
            caps["automationName"] = "uiautomator2"
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
            self.driver.implicitly_wait(10)
        else:
            self.driver.launch_app()
        return self
    def restart(self):
        self.driver.quit()
        self.driver.launch_app()
        return self
    def stop(self):
        self.driver.quit()
        return self

    def goto_main(self)->MainPage:
        return MainPage(self.driver)
