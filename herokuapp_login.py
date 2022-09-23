import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    #FORM_AUTHENTICATION = (By.XPATH, '//a[@href="/login"]')
    BOLD_TEXT = (By.XPATH, '//h2')
    EXPLICATION_TEXT = (By.XPATH, '//h4')
    LOGIN_BUTTON = (By.XPATH, '//button[@class="radius"]')
    CHECK_ELEMENTAL_HREF = (By.XPATH, '//a[@href = "http://elementalselenium.com/"]')
    USER = (By.XPATH, '//input[@id="username"]')
    PASS = (By.XPATH, '//input[@id="password"]')
    BOLD_LOGIN = (By.XPATH, '//h2')
    LOGOUT = (By.XPATH, '//a[@class="button secondary radius"]')
    LOGOUT_MESSAGE = (By.ID,'flash')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get("https://the-internet.herokuapp.com/login")
        self.chrome.implicitly_wait(10)

    def tearDown(self):
        sleep(2)
        self.chrome.quit()

    def test_check_url(self):
        expected_url = "https://the-internet.herokuapp.com/login"
        actual_url = self.chrome.current_url
        self.assertEqual(expected_url,actual_url, "URL is incorrect!")
        print('URL is correct!')

    def test_page_title(self):
        expected_title = "The Internet"
        actual_title = self.chrome.title
        self.assertEqual(expected_title, actual_title, "The title is incorrect!")
        print('Title is correct!')

    def test_bold_text(self):
        actual_text = self.chrome.find_element(*self.BOLD_TEXT).text
        print(actual_text)
        expected_text = "Login Page"
        self.assertEqual(expected_text, actual_text, f'The text is not correct!')
        print('Bold Text is correct!')


    def test_explication_text(self):
        actual_text = self.chrome.find_element(*self.EXPLICATION_TEXT).text
        expected_text = "This is where you can log into the secure area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages."
        self.assertEqual(expected_text, actual_text, f'The explication text is not correct!')
        print('Explication Text is correct!')

    def test_button_displayed(self):
        element = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(element.is_displayed(), "The Login button is missing!")
        print('The login button is displayed!')


    def test_check_attribute_href(self):
        the_link = self.chrome.find_element(*self.CHECK_ELEMENTAL_HREF).get_attribute('href')
        assert the_link == "http://elementalselenium.com/", f"The link is not correct"
        print('Elemental href is correct!')

    def test_login(self):
        self.chrome.find_element(*self.USER).send_keys("tomsmith")
        self.chrome.find_element(*self.PASS).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

    def test_bold_login(self):
        self.chrome.find_element(*self.USER).send_keys("tomsmith")
        self.chrome.find_element(*self.PASS).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual_text = self.chrome.find_element(*self.BOLD_LOGIN).text
        expected_text = "Secure Area"
        self.assertEqual(expected_text, actual_text, f'The bold login text is not correct!')
        print('The bold login text is correct!')

    def test_click_logout(self):
        self.chrome.find_element(*self.USER).send_keys("tomsmith")
        self.chrome.find_element(*self.PASS).send_keys("SuperSecretPassword!")
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT).click()
        logout_message = self.chrome.find_element(*self.LOGOUT_MESSAGE)
        assert logout_message.is_displayed(), f'Mesajul nu este afisat!'
        print(logout_message.text)
        print('Mesajul este afisat')


