class Base:
    def __init__(self, driver):
        self.driver = driver
        #print("in base room")

    def element(self, indicator):
        if indicator[0] == "ID":
            return self.driver.find_element_by_id(indicator[1])
        elif indicator[0] == "ACCESS":
            return self.driver.find_element_by_accessibility_id(indicator[1])
        elif indicator[0] == "UI_ID_mul":
            return self.driver.find_elements_by_android_uiautomator(
                'new UiSelector().resourceId("' + indicator[1] + '")')


class HomePage(Base):
    locators = {
        "Search_btn": ["ID", "com.whatsapp:id/menuitem_search"],
        "More_option_btn": ["ACCESS", "More options"],
        "More_options": ["UI_ID_mul", "com.whatsapp:id/title"],
        "Search_box": ["ID", "com.whatsapp:id/search_src_text"],
        "results": ["UI_ID_mul", "com.whatsapp:id/conversations_row_contact_name"]
    }

    def __init__(self, driver):
        super().__init__(driver)
        #print("homepage constructor")

    def get_element(self, indicator):
        if indicator in self.locators:
            return self.element(self.locators[indicator])


class Receiver(Base):
    locators = {
        "Contact_name": ["ID", "com.whatsapp:id/conversation_contact_name"],
        "Entry": ["ID", "com.whatsapp:id/entry"],
        "V_rec": ["ID", "com.whatsapp:id/voice_note_btn"],
        "Send": ["ID", "com.whatsapp:id/send"]
    }

    def __init__(self, driver):
        super().__init__(driver)
        #print("search_box constructor")

    def get_element(self, indicator):
        if indicator in self.locators:
            return self.element(self.locators[indicator])
