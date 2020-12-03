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



class Test_004_DirectEstimatorLeadFlow:
    baseURL="https://wip.d1an3ax2xglzwd.amplifyapp.com"
    username="venki"
    password="Venki@123"
    searchCID="6988881"

    def test_DirectEstimatorLeadFlow(self,setup):
         #self.driver=webdriver.chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(7)
        self.lp=Login(self.driver)
        assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/login" in self.driver.current_url
        print(self.driver.current_url)
        time.sleep(7)
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(5)
        assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/dashboard" in self.driver.current_url
        print(self.driver.current_url)
        time.sleep(5)

        self.lf = LeadFlow(self.driver)

        self.lf.clickSearchButton()
        time.sleep(5)
        self.lf.setSearchCID(self.searchCID)
        time.sleep(5)
        self.lf.clickSearchIcon()
        time.sleep(5)
        self.lf.clickSearchResult()
        time.sleep(15)
        text_element = self.driver.find_element_by_id("custName").text
        print(text_element)
        assert "Customer Name : venki" in text_element

        text_element1 = self.driver.find_element_by_id("cid").text
        print(text_element1)
        assert "6988881Branch : Dallas" in text_element1

        text_element2 = self.driver.find_element_by_id("scriptcardtext").text
        print("Call page Script card : ", text_element2)
        assert '"All My Sons Moving & Storage!\nThis is V venkatesh, I can definitely help you!"'in text_element2

        self.lf.clickNewOpportunity()
        time.sleep(5)

        text_element3 = self.driver.find_element_by_id("scriptcardtext").text
        print("Customer Info Script card : ", text_element3)
        assert "And who am I speaking with today?" in text_element3

        self.lf.clickNameandPhonepageContinueButton()
        time.sleep(3)

        text_element4 = self.driver.find_element_by_id("scriptcardtext").text
        print("moved-with-us Script card : ", text_element4)
        assert "Have you moved with us before?" in text_element4

        self.lf.clickYesButton()
        time.sleep(5)

        #text_element5 = self.driver.find_element_by_id("scriptcardtext").text
        #print("welcome-back Script card : ", text_element5)
        #assert '"Welcome back! Looking forward to providing you a great experience again.\n\nI also want you to have peace of mind th...r employees are healthy and our customers are safe.\n\nLet me quickly gather your information and get\nyou scheduled."' in text_element5

        self.lf.clickYesContinueButton()
        time.sleep(2)

        text_element6 = self.driver.find_element_by_id("scriptcardtext").text
        print("move-type Script card : ", text_element6)
        assert "Are we moving you from a..." in text_element6

        self.lf.clickOnHouse()
        time.sleep(7)

        text_element8 = self.driver.find_element_by_id("scriptcardtext").text
        print("moving-from Script card : ", text_element8)
        assert "And what's the address you're moving from?" in text_element8

        self.lf.clickonAddresspageContinueButton()
        time.sleep(2)

        text_element9 = self.driver.find_element_by_id("scriptcardtext").text
        print("VerifyHouseInfo Script card : ", text_element9)
        assert "Let's verify your information" in text_element9

        self.lf.clickonVerifyHouseButton()
        time.sleep(5)

        text_element10 = self.driver.find_element_by_id("scriptcardtext").text
        print("entire-move Script card : ", text_element10)
        assert "Are we going to be moving everything for you, or\nis this a partial move?" in text_element10

        self.lf.clickonYesEntireHome()
        time.sleep(20)

        text_element11 = self.driver.find_element_by_id("scriptcardtext").text
        print("move-date Script card : ", text_element11)
        assert "And what day are you looking\nfor us to move you?" in text_element11

        self.lf.clickonExactdate()
        time.sleep(20)
        text_element12 = self.driver.find_element_by_id("scriptcardtext").text
        print("set-estimator Script card : ", text_element12)
        assert '"Shannon is one of our best estimator and available to survey your home.\n1 Years with All My Sons. Any additional information about estimator goes here"'in text_element12


