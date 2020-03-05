from whatsapp import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.locator = Locators.HomePage(driver)

    def search_btn(self):
        return self.locator.get_element("Search_btn")

    def search_click(self):
        self.locator.get_element("Search_btn").click()
        return self.locator.get_element("Search_box")

    def search(self, reciever):
        #self.locator.get_element("Search_btn").click()
        element = self.locator.get_element("Search_box")
        element.send_keys(reciever)
        return element

    def result(self):
        #print(self.locator.get_element("results"))
        print(len(self.locator.get_element("results")))
        return self.locator.get_element("results")

    def click_result(self, index):
        return self.locator.get_element("results")[index]
