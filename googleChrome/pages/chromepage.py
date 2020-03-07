from googleChrome import locators

class Homepage:

    def __init__(self,driver):
        self.driver = driver
        self.chrome_home = locators.home_page(driver)

    def home_btn(self):
        return self.chrome_home.get_element("home")

    def more_option_click(self):
        self.chrome_home.get_element("more_option_btn").click()
        return self.chrome_home.get_element("more_options")

    def click_menue_option(self, option):
        self.chrome_home.get_element("more_options")[option].click()
