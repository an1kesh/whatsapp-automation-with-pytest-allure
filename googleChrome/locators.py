class base:
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




class home_page(base):
    locators = {
        "more_option_btn" : ["ACCESS", "More options"],
        "more_options": ["UI_ID_mul_re", "com.android.chrome:id/menu_item_text"],
        "menu": ["UI_ID_mul_re", "android:id/title"],
        "tab": ["ID", "com.android.chrome:id/tab_switcher_button"],
        "home":["ID", "com.android.chrome:id/home_button"]
    }

    def __init__(self, driver):
        super().__init__(driver)

    def get_element(self, indicator):
        if indicator in self.locators:
            return self.element(self.locators[indicator])

class setting_page(base):
    locators = {
        "Theme_btn": ["ID", "com.android.chrome:id/dark"],
        "back": ["UI_ID_mul_cl", "android.widget.ImageButton"]
    }

    def __init__(self, driver):
        super().__init__(driver)

    def get_element(self, indicator):
        if indicator in self.locators:
            return self.element(self.locators[indicator])