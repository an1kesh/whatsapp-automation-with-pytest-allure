'''

caps = {
          "platformName": "android",
          "platformVersion": "9.0",
          "deviceName": "Redmi",
          "deviceId": "192.168.0.105:5555",
          "appPackage": "com.whatsapp",
          "appActivity": "com.whatsapp.HomeActivity",
          "noReset": "true"
    }
    global driver
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)


#home = Locators.HomePage(driver)
    #home.get_element("Search_btn", driver).click()


print(driver.find_element_by_id("com.whatsapp:id/tab").text)
#driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("com.whatsapp:id/tab").text("CALLS")')[0].click()
#print(el)
#print(type(el))
#l2print(driver.find_element_by_id("com.whatsapp:id/menuitem_search"))
#driver.find_element_by_accessibility_id("More options").click()
driver.find_element_by_id("com.whatsapp:id/menuitem_search").click()
driver.find_element_by_id("com.whatsapp:id/search_src_text").send_keys(user)
#print(driver.find_element_by_id("com.whatsapp:id/contact_row_container").text)
driver.find_element_by_id("com.whatsapp:id/contact_row_container").click()
driver.find_element_by_id("com.whatsapp:id/entry").send_keys("xcz")
driver.find_element_by_id("com.whatsapp:id/send").click()
driver.find_element_by_id("com.whatsapp:id/back").click()



class Search_box(Base):
    locators = {
        "Search_box": ["ID", "com.whatsapp:id/search_src_text"],
        "results": ["UI_ID_mul", "com.whatsapp:id/conversations_row_contact_name"]
    }

    def __init__(self, driver):
        super().__init__(driver)
        print("search_box constructor")

    def get_element(self, indicator, driver):
        if indicator in self.locators:
            return self.element(self.locators[indicator])




from appium import webdriver


def get_driver():
    caps = {
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Redmi",
        "deviceId": "febeuwguzlfu7ppb",
        "appPackage": "com.instagram.android",
        "appActivity": "com.instagram.mainactivity.MainActivity",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    return driver


def test():
    driver = get_driver()
    driver.find_elements_by_android_uiautomator(
        'new UiSelector().className("android.widget.FrameLayout").description("Camera")')[0].click()

    # driver.find_element_by_class_name("android.widget.FrameLayout").



test()

'''
