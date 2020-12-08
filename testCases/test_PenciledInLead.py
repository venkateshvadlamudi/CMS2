import time

import pytest
from selenium import webdriver

import utilities
from pageObjects.LeadFlowPage import LeadFlow
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

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_003_PenciledInLeadFlow:
    baseURL="foo"
    username="venki"
    password="Venki@123"
    searchCID="6988880"

    def test_PenciledInLeadFlow(self,setup):
         #self.driver=webdriver.chrome()
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/login" in self.driver.current_url
        print(self.driver.current_url)
        self.lp.setUserName(self.username)

        self.lp.setPassword(self.password)

        self.lp.clickLogin()

        print(self.driver.current_url)

        self.lf = LeadFlow(self.driver)

        self.lf.clickSearchButton()

        self.lf.setSearchCID(self.searchCID)

        self.lf.clickSearchIcon()

        self.lf.clickSearchResult()


        assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/penciled-in/PenciledInLead" in self.driver.current_url
        print(self.driver.current_url)

        text_element = self.driver.find_element_by_id("scriptcardtext").text
        print("PenciledInLead Script Card : ", text_element)
        assert '"All My Sons Moving & Storage!\nThis is V venkatesh, how can I help you?\n\nGreat, is this Test?\n\nWonderful! I have all your information already\npulled up. Let’s confirm and get you scheduled. I\nsee you’re doing a..."' in text_element


        text_element1 = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]").text
        print("move-type  : ", text_element1)
        assert "INTERSTATE" in text_element1

        text_element2 = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/li[1]/div[2]/div[1]/div[1]").text
        print("From Address  : ", text_element2)
        assert "Dallas, TX 75201, USA" in text_element2

        text_element3 = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/li[1]/div[2]/div[1]/div[1]").text
        print("To Address  : ", text_element3)
        assert "MERRIONETT PK, IL 60803, USA" in text_element3

        text_element4 = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/li[1]/div[2]/div[1]/div[1]").text
        print("Move Date  : ", text_element4)
        assert "Wednesday, 12/30" in text_element4

        text_element5 = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[5]/li[1]/div[2]/div[1]").text
        print("Phone number  : ", text_element5)
        assert "(788) 999-9999" in text_element5

        text_element6 = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[6]/li[1]/div[2]/div[1]/div[1]").text
        print("Rate : ", text_element6)
        assert "3 Men at $159/Hr." in text_element6

        text_element7 = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[7]/li[1]/div[2]/div[1]/div[1]").text
        print("Hours", text_element7)
        assert "20 HR" in text_element7

        bookNowButton = self.driver.find_element_by_id("BOOKNOW").text
        assert "BOOK NOW" in bookNowButton
        print(bookNowButton)

        setforestimatorButton = self.driver.find_element_by_id("setforestimator").text
        assert "SET FOR ESTIMATOR" in setforestimatorButton
        print(setforestimatorButton)

        noButton = self.driver.find_element_by_id("NO").text
        assert "NO" in noButton
        print(noButton)



