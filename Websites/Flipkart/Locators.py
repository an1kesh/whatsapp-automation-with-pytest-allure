
class Base:
    def __init__(self, driver):
        self.driver = driver
        print("in level")

    def element(self, indicator):
        if indicator[0] == "ID":
            return self.driver.find_element_by_id(indicator[1])
        elif indicator[0] == "ACCESS":
            return self.driver.find_element_by_accessibility_id(indicator[1])
        elif indicator[0] == "UI_ID_mul_re":
            return self.driver.find_elements_by_android_uiautomator(
                'new UiSelector().resourceId("' + indicator[1] + '")')
        elif indicator[0] == "UI_ID_mul_cl":
            return self.driver.find_element_by_Xpath(indicator[1])





class flipLogin(Base):
    locators = {
        "login_btn": ["XPATH", "//a[@class='_3NH1qf _2x71WM']"],
        "email_use": ["XPATH", "//span[@class='_3ZN6CT _P1NtA']"],
        "Username_text": ["XPATH", "//input[@class='_1i5zkb']"],
        "continue": ["XPATH", "//button[@class='_2iUM2T LuQr2v']"],
        "password": ["XPATH", "//input[@class='_1i5zkb']"]
    }

    def __init__(self, driver):
        super().__init__(driver)
        print("homepage constructor")

    def get_element(self, indicator):
        if indicator in self.locators:
            return self.element(self.locators[indicator])


class flipLogout(Base):
    locators = {
        "profile_btn": ["XPATH", "(//a[@class='_3NH1qf'])[5]"],
        "Entry": ["ID", "com.whatsapp:id/entry"],
        "V_rec": ["ID", "com.whatsapp:id/voice_note_btn"],
        "Send": ["ID", "com.whatsapp:id/send"]
    }

    def __init__(self, driver):
        super().__init__(driver)
        print("search_box constructor")

    def get_element(self, indicator):
        if indicator in self.locators:
            return self.element(self.locators[indicator])