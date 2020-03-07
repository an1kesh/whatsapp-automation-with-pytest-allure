import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class flipLogin:

    def __init__(self,driver):
        self.driver= driver

    def login(self):
        self.driver.get("https://flipkart.com/")
        self.driver.find_element(By.XPATH, "//a[@class='_3NH1qf _2x71WM']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//span[@class='_3ZN6CT _P1NtA']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@class='_1i5zkb']").send_keys("piyushjuneja9@gmail.com")
        self.driver.find_element(By.XPATH, "//button[@class='_2iUM2T LuQr2v']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@class='_1i5zkb']").send_keys("juneja23piyush")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//input[@class='_1i5zkb']").send_keys(Keys.ENTER)
        time.sleep(3)