import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class flipLogout:

    def __init__(self,driver):
        self.driver= driver

    def logout(self):
        self.driver.find_element(By.XPATH, "(//a[@class='_3NH1qf'])[5]").click()
        time.sleep(2)
        self.driver.execute_script("mobile: scroll", {"direction": "down"})
        # driver.find_element_by_link_text("logout-23998873").click()
        time.sleep(2)
        element1 = self.driver.find_element_by_xpath("//div[@class='_3L9xZy']")
        element2 = self.driver.find_element_by_xpath("(//div[@class='_3ulu7X'])[5]")
        TouchAction(self.driver).press(element1).move_to(element2).release().perform()
