from googleChrome import locators

class SettingPage:

    def __init__(self,driver):
        self.driver = driver
        self.settiings = locators.setting_page(driver)

    def back_btn(self):
        return self.settiings.get_element("back")

    def click_back_btn(self):
        self.settiings.get_element("back").click()

    def theme_btn(self):
        return self.settiings.get_element("Theme_sel")

    def theme_btn(self):
        self.settiings.get_element("Theme_sel").click()

    def click_menue_option(self, option):
        self.chrome_home.get_element("more_options")[option].click()
