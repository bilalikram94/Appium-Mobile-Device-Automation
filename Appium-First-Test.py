import unittest
import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time


class Today_Today(unittest.TestCase):
    reportDirectory = 'reports'
    reportFormat = 'xml'
    dc = {}
    testName = 'Today_Today'
    driver = None

    def setUp(self):
        self.dc['reportDirectory'] = self.reportDirectory
        self.dc['reportFormat'] = self.reportFormat
        self.dc['testName'] = self.testName
        self.dc['udid'] = 'FFY5T17C23020810'
        self.dc['appPackage'] = 'com.todaytoday'
        self.dc['appActivity'] = '.MainActivity'
        self.dc['platformName'] = 'android'
        self.dc['version'] = '8.0.0'
        self.dc['deviceName'] = 'RNE-L21'
        self.driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub', self.dc)
        print("jsu testing", self.driver)
        time.sleep(3)

    def testToday_Today(self):
        self.driver.switch_to.context("NATIVE_APP")
        time.sleep(5)
        self.driver.find_elements_by_xpath("//*[@text='SHOP NOW']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@text='Categories']")))
        self.driver.find_element_by_xpath("//*[@x='846']").click()
        self.driver.find_element_by_xpath("//*[@x='48']").click()
        self.driver.find_element_by_xpath("//*[@x='48']").click()
        self.driver.find_element_by_xpath("//*[@x='48']").click()
        self.driver.find_element_by_xpath("//*[@text='Email address']").send_keys('muneeb.riaz@cubixlabs.com')
        self.driver.find_element_by_xpath("//*[@text='Password']").send_keys('muneeb@123')
        self.driver.find_element_by_xpath("//*[@text='SIGN IN']").click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
