import time

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def get_driver():
    caps = {
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Redmi",
        "deviceId": "febeuwguzlfu7ppb",
        #"deviceId":"d91bcc76",
        #"deviceID":"jvlrwwpzs8jnnj5p",
        "browserName": "Chrome",
        "noReset": "true"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
    return driver


def test():
    driver = get_driver()

    print(driver.contexts)
    print(driver.context)

    print(driver.contexts)
    print(driver.switch_to.context(driver.contexts[0]))
    print(driver.context)
    driver.find_element_by_accessibility_id("More options").click()
    print(driver.find_elements_by_android_uiautomator(
        'new UiSelector().resourceId("com.android.chrome:id/menu_item_text")')[8].text)
    """

    driver.find_element_by_accessibility_id("More options").click()
    driver.find_elements_by_android_uiautomator(
        'new UiSelector().resourceId("com.android.chrome:id/menu_item_text").text("Settings")')[0].click()
    driver.find_elements_by_android_uiautomator(
        'new UiSelector().resourceId("android:id/title").text("Themes")')[0].click()
    
    driver.find_element_by_id("com.android.chrome:id/dark").click()
    driver.find_elements_by_android_uiautomator(
       'new UiSelector().className("android.widget.ImageButton").description("Navigate up")')[0].click()
    driver.find_elements_by_android_uiautomator(
        'new UiSelector().className("android.widget.ImageButton").description("Navigate up")')[0].click()
    
    print(driver.switch_to.context(driver.contexts[1]))
    print(driver.context)"""
    #FLIPKART

    driver.get("https://flipkart.com/")

    time.sleep(5)



    """driver.find_element(By.XPATH, "//a[@class='_3NH1qf _2x71WM']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[@class='_3ZN6CT _P1NtA']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//input[@class='_1i5zkb']").send_keys("piyushjuneja9@gmail.com")
    driver.find_element(By.XPATH,"//button[@class='_2iUM2T LuQr2v']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@class='_1i5zkb']").send_keys("juneja23piyush")
    time.sleep(3)
    driver.find_element(By.XPATH, "//input[@class='_1i5zkb']").send_keys(Keys.ENTER)
    time.sleep(3)
    driver.find_element(By.XPATH, "(//a[@class='_3NH1qf'])[5]").click()
    time.sleep(2)
    driver.execute_script("mobile: scroll", {"direction": "down"})
    #driver.find_element_by_link_text("logout-23998873").click()
    time.sleep(2)
    element1 = driver.find_element_by_xpath("//div[@class='_3L9xZy']")
    element2 = driver.find_element_by_xpath("(//div[@class='_3ulu7X'])[5]")
    TouchAction(driver).press(element1).move_to(element2).release().perform()"""




test()