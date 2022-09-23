import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Test1(unittest.TestCase):
    # FIRST_NAME = (By.XPATH, '//input[@name="first_name"]')
    # LAST_NAME = (By.XPATH, '//input[@name="last_name"]')
    # PHONE = (By.XPATH, '//input[@name="phone"]')
    # EMAIL = (By.XPATH, '//input[@name="email"]')
    # HUMAN = (By.XPATH, '//div[@class="recaptcha-checkbox-borderAnimation"]')
    # CLICK_SIGNUP = (By.XPATH, '//span[contains(text(),"Signup")]')
    USER_PLACEHOLDER = (By.XPATH, "//label[contains(text(),'Email')]")
    PASS_PLACEHOLDER = (By.XPATH, "//label[contains(text(),'Password')]")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://phptravels.net/login/signup")
        sleep(3)

    def tearDown(self):
        self.chrome.quit()

    # def completeaza_date(self):
    #     self.chrome.find_element(*self.FIRST_NAME).send_keys('Mihai')
    #     sleep(2)
    #     self.chrome.find_element(*self.LAST_NAME).send_keys('Lacriceanu')
    #     sleep(2)
    #     self.chrome.find_element(*self.PHONE).send_keys('123456789')
    #     sleep(2)
    #     self.chrome.find_element(*self.EMAIL).send_keys('abc@gmail.com')
    #     sleep(2)
    #     self.chrome.find_element(*self.HUMAN).click()
    #     sleep(2)
    #     self.chrome.find_element(*self.CLICK_SIGNUP).click()
    #     sleep(2)

    def test_user(self):
        actual_text = self.chrome.find_element(*self.USER_PLACEHOLDER).text
        expected_text = 'Email'
        print(actual_text)
        self.assertEqual(actual_text, expected_text,'Text incorect!')

    def test_password(self):
        actual_text = self.chrome.find_element(*self.PASS_PLACEHOLDER).text
        expected_text = 'Password'
        self.assertEqual(actual_text, expected_text, 'Text incorect!')

    def test_login(self):
        login = self.chrome.find_elements(*self.LOGIN_BUTTON)
        button = login[0]
        assert button.is_displayed(), f'Butonul de login nu este afisat!'
        print('Butonul e afisat!')
