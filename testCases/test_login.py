import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import os

class Test_001_Login:
    baseURL="https://wip.d1an3ax2xglzwd.amplifyapp.com"
    username="venki"
    password="Venki@123"



    def test_homepageTitle(self,setup):
        #self.driver=webdriver.chrome()
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        self.driver.close()
        if act_title=="CMS - All My Sons Moving and Storage":
            assert True
        else:
            assert False

    def test_login(self,setup):
         #self.driver=webdriver.chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(15)
        self.lp=Login(self.driver)
        time.sleep(10)
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        self.driver.close()











