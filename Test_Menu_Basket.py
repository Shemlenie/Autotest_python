# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

url="C:\\Users\\Glebo\\OneDrive\\Рабочий стол\\UIR\\chromedriver.exe"

class Test_Menu_Basket(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_menu_basket(self):
        driver = self.driver
        driver.get("http://localhost:8080/menu")
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div/div[2]/div/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div/div[2]/div[2]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div/div[2]/div[3]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div/div[2]/div[4]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div/div[2]/div[5]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div/div[2]/div[6]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[2]/div[2]/div/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[2]/div[2]/div[2]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[2]/div[2]/div[3]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[2]/div[2]/div[4]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[3]/div[2]/div/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[3]/div[2]/div[2]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[3]/div[2]/div[3]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[4]/div[2]/div/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[4]/div[2]/div[2]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[4]/div[2]/div[3]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[5]/div[2]/div/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[5]/div[2]/div[2]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[5]/div[2]/div[3]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[5]/div[2]/div[4]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[5]/div[2]/div[5]/div[3]/i").click()
        driver.find_element_by_xpath("//div[@id='app']/section/header/div/div/i").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys("Holywood")
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div/div[4]/button").click()
        driver.find_element_by_xpath("//button/div").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to.alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
