import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Test3(unittest.TestCase):
    USER_LOGARE = (By.ID, 'user-name')
    PAROLA_LOGARE = (By.ID,'password')
    CLICK_LOGIN = (By.ID,'login-button')
    SORTARE_CRESCATOR_PRET = (By.XPATH, '//select/option[3]')
    ADAUGA_PRODUS1 = (By.ID, 'add-to-cart-sauce-labs-onesie')
    ADAUGA_PRODUS2 = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    CLICK_COS = (By.XPATH, '//a[@class="shopping_cart_link"]')
    CHECKOUT = (By.ID, 'checkout')
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    COD_POSTAL = (By.ID, 'postal-code')
    CLICK_CONTINUE = (By.ID, 'continue')
    FINISH_ORDER = (By.ID, 'finish')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://www.saucedemo.com/")
        sleep(3)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_complete_form(self):
        self.chrome.find_element(*self.USER_LOGARE).send_keys("standard_user")
        sleep(2)
        self.chrome.find_element(*self.PAROLA_LOGARE).send_keys("secret_sauce")
        sleep(2)
        self.chrome.find_element(*self.CLICK_LOGIN).click()
        sleep(2)
        self.chrome.find_element(*self.SORTARE_CRESCATOR_PRET).click()
        sleep(2)
        self.chrome.find_element(*self.ADAUGA_PRODUS1).click()
        sleep(2)
        self.chrome.find_element(*self.ADAUGA_PRODUS2).click()
        sleep(2)
        self.chrome.find_element(*self.CLICK_COS).click()
        sleep(2)
        self.chrome.find_element(*self.CHECKOUT).click()
        sleep(2)
        self.chrome.find_element(*self.FIRST_NAME).send_keys('Mihai')
        sleep(2)
        self.chrome.find_element(*self.LAST_NAME).send_keys('Lacriceanu')
        sleep(2)
        self.chrome.find_element(*self.COD_POSTAL).send_keys('200716')
        sleep(2)
        self.chrome.find_element(*self.CLICK_CONTINUE).click()
        sleep(2)
        self.chrome.find_element(*self.FINISH_ORDER).click()
        sleep(2)