# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

url="C:\\Users\\Glebo\\OneDrive\\Рабочий стол\\UIR\\chromedriver.exe"

class Test_Reg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(url)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_reg_correct_min_1(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Ni", "White", "9120120122", "testr@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_correct_middle_1(self):
        driver = self.driver
        temp_number = 4

        for i in range(10):
            self.open_menu_page(driver, "http://localhost:8080/menu")
            self.registration(driver, "Nigger", "White", temp_number, f"test{i}@mail.ru", "12345678")
            self.logout(driver)
            temp_number = temp_number + 1

    def test_reg_correct_max_1(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Niggerrrrrrrrrr", "White", "9233393996", "testt@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_empty_2(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "", "", "", "", "")
        self.logout(driver)

    def test_reg_incorrect_first_name_min_3(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "N", "White", "9998887744", "testw@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_incorrect_first_name_max_3(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "NNNNNNNNNNNNNNNN", "White", "9998887743", "testq@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_incorrect_second_name_min_4(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Nigger", "W", "9998887742", "testa@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_incorrect_second_name_min_4(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Nigger", "Wwwwwwwwwwwwwwww", "9998887741", "testd@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_incorrect_phone_number_min_5(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Nigger", "White", "9133594096", "testqwe@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_incorrect_phone_number_max_5(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Nigger", "White", "1111111111111111111", "test5@mail.ru", "12345678")
        self.logout(driver)

    def test_reg_incorrect_mail_6(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Nigger", "White", "89133694096", "testads@mail....ru", "12345678")
        self.logout(driver)

    def test_reg_incorrect_password_min_7(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Nigger", "White", "89153694096", "testzxc@mail.ru", "1234567")
        self.logout(driver)

    def test_reg_incorrect_password_max_7(self):
        driver = self.driver
        self.open_menu_page(driver, "http://localhost:8080/menu")
        self.registration(driver, "Nigger", "White", "89154694096", "testzg@mail.ru", "1234567890123456789012345678901")
        self.logout(driver)

    # def test_reg_incorrect_first_name_3(self):
        # driver = self.driver
        # self.open_menu_page(driver, "http://localhost:8080/menu")
        # self.registration(driver, "N", "White", "100001", "test2@mail.ru", "12345678")
        # self.logout(driver)

    def open_menu_page(self, driver, url):
        driver.get(url)

    def registration(self, driver, first_name, second_name, phone_number, mail, password):
        # Имя
        driver.find_element_by_xpath("//div[@id='app']/section/header/div/div/button[2]").click()
        driver.find_element_by_xpath("//input[@type='text']").click()
        driver.find_element_by_xpath("//input[@type='text']").clear()
        driver.find_element_by_xpath("//input[@type='text']").send_keys(first_name)
        # Фамилия
        driver.find_element_by_xpath("(//input[@type='text'])[2]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys(second_name)
        # Номер телефона
        driver.find_element_by_xpath("(//input[@type='text'])[3]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[3]").send_keys(phone_number)
        # Почта
        driver.find_element_by_xpath("(//input[@type='text'])[4]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(mail)
        # Пароль
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys(password)
        # Зарегистрироваться
        driver.find_element_by_xpath("//div[@id='app']/section/section/section/div[2]/div/div[7]/button").click()

    def logout(self, driver):
        driver.find_element_by_xpath("//div[@id='app']/section/header/div/div/i[3]").click()

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