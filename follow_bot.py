from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from functions import find_and_click, input_data
from dotenv import load_dotenv
import os

# Uploading env data
load_dotenv(".env")

# Setting driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class FollowBot:
    """Bot which opens logs in to the provided instagram account, opens chosen account's followers tab and
     follows account's followers"""

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com/")
        self.wait = WebDriverWait(self.driver, 10)
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")

    def logging_in(self, insta_account):
        """Logging in with delay"""
        find_and_click(self.wait, EC, By.CSS_SELECTOR, "button[class*='_a9_0']")  # cookies agreement
        time.sleep(2)
        input_data(self.wait, EC, By.NAME, "username", self.email)  # entering username
        time.sleep(2)
        input_data(self.wait, EC, By.NAME, "password", self.password, Keys.ENTER)  # entering password
        time.sleep(5)
        self.driver.get(insta_account)  # directing to the provided instagram account

    def follow(self, account_name):
        """Opens followers tab and follows accounts from the list"""

        find_and_click(self.wait, EC, By.CSS_SELECTOR, f"a[href='/{account_name}/followers/']")  # website redirect
        time.sleep(3)

        buttons = self.driver.find_elements(By.CSS_SELECTOR, "._acan._acap._acas._aj1-._ap30")  # follow buttons

        for button in buttons:
            try:
                self.driver.execute_script("arguments[0].click();", button)  # clicking with java
                time.sleep(2)
            except Exception as e:
                print(f"Problem with clicking the button: {e}")

    def cookies(self, website):
        """Cookies add function"""
        cookies = self.driver.get_cookies()
        self.driver.get(f"https://www.instagram.com/{website}/")
        for cookie in cookies:
            self.driver.add_cookie(cookie)


