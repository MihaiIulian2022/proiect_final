import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Alerts(unittest.TestCase):
    ALERT = (By.XPATH, '//button[text()="Click for JS Alert"]')
    CONFIRM = (By.XPATH, '//button[text()="Click for JS Confirm"]')
    PROMPT = (By.XPATH, '//button[text()="Click for JS Prompt"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_alert(self):
        self.chrome.find_element(*self.ALERT).click()
        sleep(2)
        obj = self.chrome.switch_to.alert
        print("Alert shows following message: " + obj.text)
        sleep(2)
        obj.accept()
        print("Clicked on the OK Button in the Alert Window")
        sleep(2)

    def test_confirm_ok(self):
        self.chrome.find_element(*self.CONFIRM).click()
        obj = self.chrome.switch_to.alert
        print(f"Alert shows following message: {obj.text}" )
        sleep(3)
        obj.accept()
        print("Clicked on the OK Button in the Confirm Window")
        sleep(3)

    def test_confirm_cancel(self):
        self.chrome.find_element(*self.CONFIRM).click()
        obj = self.chrome.switch_to.alert
        print("Confirm shows following message: " + obj.text)
        sleep(3)
        obj.dismiss()
        print("Clicked on the Cancel Button in the Confirm Window")
        sleep(3)

    def test_prompt(self):
        self.chrome.find_element(*self.PROMPT).click()
        sleep(2)
        obj = self.chrome.switch_to.alert
        print("Prompt shows following message: " + obj.text)
        obj.send_keys('Mihai')
        obj.accept()
        print("Clicked on the OK Button in the Prompt Window")
        sleep(3)