import os

from appium import webdriver


class Utilll():

    @staticmethod
    def get_driver(platform):
        if platform == "android":
            caps = {
                "platformName": "android",
                "platformVersion": "9.0",
                "deviceName": "Redmi",
                #"deviceId": "d91bcc76",
                "deviceId": "febeuwguzlfu7ppb",
                "appPackage": "com.whatsapp",
                "appActivity": "com.whatsapp.HomeActivity",
                "noReset": "true"
            }
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            #driver.find_element_by_class_name().get_attribute()
            return driver
        elif platform == "IOS":
            app = os.path.join(os.path.dirname(__file__),
                               'TableSearchwithUISearchController/Swift',
                               'Search.swift.app')
            app = os.path.abspath(app)
            caps = {
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '9.2',
                'deviceName': 'iPhone 5s',
                'bundleId':'com.example.apple-samplecode.Search-swift'
            }
            driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            return driver

