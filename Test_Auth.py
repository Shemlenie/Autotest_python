# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

url="C:\\Users\\Glebo\\OneDrive\\Рабочий стол\\UIR\\chromedriver.exe"

class TestAuth(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(url)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_auth_correct_1(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.auth(driver, "test1@mail.ru", "12345678")

    def test_auth_incorrect_2(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.auth(driver, "test1111111@mail.ru", "12345678222")

    def open_menu_page(self, driver, url):
        driver.get(url)

    def auth(self, driver, mail, password):
        # Почта
        driver.find_element_by_xpath("//div[@id='app']/section/header/div/div/button").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(mail)
        # Пароль
        # time.sleep(5)
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[2]/div/div[4]/button").click()

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
            alert = self.driver.switch_to_alert()
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
