import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Test2(unittest.TestCase):
    COMPLETE_WEB_FORM = (By.XPATH, '//a[@class="btn btn-lg"]//parent::li//following-sibling::li[13]/a')
    ENTER_FIRST_NAME = (By.ID,'first-name')
    ENTER_LAST_NAME = (By.ID,'last-name')
    ENTER_JOB_TITLE = (By.ID,'job-title')
    ENTER_EDUCATION = (By.ID,'radio-button-3')
    ENTER_SEX = (By.ID,'checkbox-1')
    ENTER_EXPERIENCE = (By.XPATH, "//select/option[2]")
    ENTER_DATE = (By.ID, 'datepicker')
    CLICK_SUBMIT_BUTTON = (By.XPATH,'//a[@role="button"]')

    def setUp(self) -> None:
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(5)
        self.chrome.get("https://formy-project.herokuapp.com/")
        self.chrome.find_element(*self.COMPLETE_WEB_FORM).click()
        sleep(3)

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_complete_form(self):
        self.chrome.find_element(*self.ENTER_FIRST_NAME).send_keys("Mihai")
        sleep(2)
        self.chrome.find_element(*self.ENTER_LAST_NAME).send_keys("Lacriceanu")
        sleep(2)
        self.chrome.find_element(*self.ENTER_JOB_TITLE).send_keys("automation tester")
        sleep(2)
        self.chrome.find_element(*self.ENTER_EDUCATION).click()
        sleep(2)
        self.chrome.find_element(*self.ENTER_SEX).click()
        sleep(2)
        self.chrome.find_element(*self.ENTER_EXPERIENCE).click()
        sleep(2)
        self.chrome.find_element(*self.ENTER_DATE).send_keys("07/20/1987")
        sleep(2)
        self.chrome.find_element(*self.CLICK_SUBMIT_BUTTON).click()
        sleep(2)



