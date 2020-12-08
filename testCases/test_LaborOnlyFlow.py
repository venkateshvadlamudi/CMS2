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


class Test_005_CouponLeadFlow:
    baseURL = "https://wip.moverfull.com/"
    username = "venki"
    password = "Venki@123"
    searchCID = "6988930"


    def test_CouponFlow(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(12)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)

        print(self.driver.current_url)

        self.lp.setUserName(self.username)

        self.lp.setPassword(self.password)

        self.lp.clickLogin()

        # assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/dashboard" in self.driver.current_url
        # self.assertIn('/dashboard', self.getUrl())
        print(self.driver.current_url)

        self.lf = LeadFlow(self.driver)

        self.lf.clickSearchButton()

        self.lf.setSearchCID(self.searchCID)

        self.lf.clickSearchIcon()

        self.lf.clickSearchResult()

        text_element = self.driver.find_element_by_id("custName").text
        print(text_element)
        assert "Customer Name : test" in text_element

        text_element1 = self.driver.find_element_by_id("cid").text
        print(text_element1)
        assert "6988930Branch : Dallas" in text_element1

        text_element2 = self.driver.find_element_by_id("scriptcardtext").text
        print("Call page Script card : ", text_element2)
        assert  '"All My Sons Moving & Storage!\nThis is venkatesh, I can definitely help you!"' in text_element2

        self.lf.clickNewOpportunity()

        text_element3 = self.driver.find_element_by_id("scriptcardtext").text
        print("Customer Info Script card : ", text_element3)
        assert "And who am I speaking with today?" in text_element3

        self.lf.clickNameandPhonepageContinueButton()

        text_element4 = self.driver.find_element_by_id("scriptcardtext").text
        print("moved-with-us Script card : ", text_element4)
        assert "Have you moved with us before?" in text_element4

        self.lf.clickYesButton()

        # text_element5 = self.driver.find_element_by_id("scriptcardtext").text
        # print("welcome-back Script card : ", text_element5)
        # assert '"Welcome back! Looking forward to providing you a great experience again.\n\nI also want you to have peace of mind th...r employees are healthy and our customers are safe.\n\nLet me quickly gather your information and get\nyou scheduled."' in text_element5

        self.lf.clickYesContinueButton()

        text_element6 = self.driver.find_element_by_id("scriptcardtext").text
        print("move-type Script card : ", text_element6)
        assert "Are we moving you from a..." in text_element6

        self.lf.clickOnApartment()

        text_element7 = self.driver.find_element_by_id("scriptcardtext").text
        print("apartment-bedrooms Script card : ", text_element7)
        assert "And how many bedrooms in your home?" in text_element7

        self.lf.clickon1bedapartment()
        time.sleep(5)

        text_element8 = self.driver.find_element_by_id("scriptcardtext").text
        print("moving-from Script card : ", text_element8)
        assert "And what's the address you're moving from?" in text_element8

        self.lf.setToAddress()
        time.sleep(5)
        self.lf.clickonlabouronly()

        text_element9 = self.driver.find_element_by_id("scriptcardtext").text
        print("apartment-floors Script card : ", text_element9)
        assert "Tell me more about your move..." in text_element9

        self.lf.clickonFloorspageContinuebutton()

        text_element10 = self.driver.find_element_by_id("scriptcardtext").text
        print("Labor-type Script card : ", text_element10)
        assert '"And what kind of labour will you need help with?"' in text_element10

        self.lf.clickonLoading()

        text_element11 = self.driver.find_element_by_id("scriptcardtext").text
        print("move-date Script card : ", text_element11)
        assert '"Are we going to be loading everything for you, or\nis this a partial load?"' in text_element11

        self.lf.clickonYesEntireHomeLoad()
        time.sleep(15)
        text_labouronlydate = self.driver.find_element_by_id("scriptcardtext").text
        print("Laboronly move-date Script card : ", text_labouronlydate)
        assert '"And what day are you looking\nfor us to help you load?"' in text_labouronlydate

        self.lf.clickonExactdate()
        time.sleep(15)

        text_element12 = self.driver.find_element_by_id("scriptcardtext").text
        print("special-reqs Script card : ", text_element12)
        assert "Do you have any items with\nspecial requirements?" in text_element12

        self.lf.clickonSpecialReqsContinueButton()

        text_element13 = self.driver.find_element_by_id("scriptcardtext").text
        print("heaviest-item Script card : ", text_element13)
        assert "And if you had to choose one, what would you say\nis the heaviest item in your home?" in text_element13

        self.lf.clickonHeaviestpageContinueButton()

        text_element14 = self.driver.find_element_by_id("scriptcardtext").text
        print("packing Script card : ", text_element14)
        assert "Now as far as packing your boxes goes,\ndo you need help packing or\nwill you pack the boxes yourself?" in text_element14

        self.lf.clickonSelfPacking()

        text_element15 = self.driver.find_element_by_id("scriptcardtext").text
        print("last-move Script card : ", text_element15)
        assert "Now test, I have a good understanding of your\nmove so far & to help make sure this is the best\nmove you’ve ever had, it would be helpful to ask you\na couple questions about your last move.\nMay I do that?" in text_element15

        self.lf.clickonlastmoveContinueButton()

        self.lf.clickonThankyoupageContinuebutton()

        time.sleep(5)

        text_element17 = self.driver.find_element_by_id("scriptcardtext").text
        print("Labor Only pricing page Script card ---->: ", text_element17)
        assert "Now for pricing test, we like to keep it very simple. I'll just have you hire us by the hour and get you started with our 2 Men 2 Hour Package. You pay a flat rate for the first 2 hours, and then an hourly rate for any time beyond 2 hours. The clock doesn't start until we arrive and begin loading" in text_element17

        text_hoursforrate = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/li[1]/div[1]/div[1]/div[2]/span[1]/div[1]").text
        print("Hours and labouronly price  --->: ", text_hoursforrate)
        assert "The flat rate for the first 2 hours is $441.18, which covers everything up to 2 hours, all on your time" in text_hoursforrate

        text_Hourlyrate = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/li[2]/div[1]/div[1]/div[2]/span[1]/div[1]").text
        print("Hourly Rate --->: ", text_Hourlyrate)
        assert "If we go beyond 2 hours, then it's all based on an Hourly Rate of just $129 per hour, pro-rated in quarter hour increments" in text_Hourlyrate

        self.lf.clickonpricingContinueButton()

        text_element18 = self.driver.find_element_by_id("scriptcardtext").text
        print("quote-booking Script card : ", text_element18)
        assert '"Again, my name is venkatesh and I’m going to be here every step of the way to make sure this is the best move you’ve ever had.'in text_element18

        self.lf.clickonquotebookingSetforestimatorButton()

