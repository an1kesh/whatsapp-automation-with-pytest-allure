from whatsapp import Locators


class ChatPage:

    def __init__(self, driver):
        self.driver = driver
        self.chat = Locators.Receiver(driver)

    def chat_name(self):
        return self.chat.get_element("Contact_name")

    def enter_msg(self, msg):
        self.chat.get_element("Entry").send_keys(msg)

    def click_send(self):
        self.chat.get_element("Send").click()