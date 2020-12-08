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
    searchCID = "6988911"

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
        assert "6988911Branch : Dallas" in text_element1

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

        text_element8 = self.driver.find_element_by_id("scriptcardtext").text
        print("moving-from Script card : ", text_element8)
        assert "And what's the address you're moving from?" in text_element8

        self.lf.clickonAddresspageContinueButton()

        text_element9 = self.driver.find_element_by_id("scriptcardtext").text
        print("apartment-floors Script card : ", text_element9)
        assert "Tell me more about your move..." in text_element9

        self.lf.clickonFloorspageContinuebutton()

        text_element10 = self.driver.find_element_by_id("scriptcardtext").text
        print("entire-move Script card : ", text_element10)
        assert "Are we going to be moving everything for you, or\nis this a partial move?" in text_element10

        self.lf.clickonYesEntireHome()
        time.sleep(15)

        text_element11 = self.driver.find_element_by_id("scriptcardtext").text
        print("move-date Script card : ", text_element11)
        assert "And what day are you looking\nfor us to move you?" in text_element11

        self.lf.clickonFlexibledate()
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

        text_element16 = self.driver.find_element_by_id("scriptcardtext").text
        print("Thankyou Script card : ", text_element16)
        assert "Thank you for sharing that with me and for considering us for your move. Let’s talk about what your move day is going to look like with All My Sons. First, we start by carefully selecting men of character to arrive in a clean, sanitized, 26ft truck with everything needed to provide you a quality job. This includes moving blankets for your furniture prevent nicks and scratches. Tools to disassemble and reassemble items such as your beds. And we will help you get settled in by placing everything in your new home where you want nice nice. On top of that, we reward our men for 5 star reviews and they earn those by moving at a fast professional pace which is what saves you money and reduces the stress of a move. That’s why we’ve been in business for 29 years with great google reviews as well as an A report with the Better Business Bureau." in text_element16

        self.lf.clickonThankyoupageContinuebutton()

        text_element17 = self.driver.find_element_by_id("scriptcardtext").text
        print("pricing Script card : ", text_element17)
        assert "Now for pricing test, we like to keep it very simple. I’ll just have you hire us by the hour. The time starts when we arrive at your home, and stops once we’re finished." in text_element17

        text_FlexableDateCoupon = self.driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/li[4]/div[1]/div[1]/div[2]/span[1]").text
        print("FlexableDateCoupon --->: ", text_FlexableDateCoupon)
        assert "The Flexible Date Coupon is available for your move. Select Jan 01, 2021 for -$60Hr Rates" in text_FlexableDateCoupon

        self.lf.clickonflexableCoupon()

        self.lf.clickonselectflexabledate()

        text_selectFlexableDatepage = self.driver.find_element_by_id( "scriptcardtext").text
        print("Select Flexable Datepage --->: ", text_selectFlexableDatepage)
        assert '"The Flexible Date Coupon is available for\nyour move. Change the move date to apply."' in text_selectFlexableDatepage

        self.lf.clickonupdatemovedate()

        #self.lf.clickonpricingContinueButton()

        text_element18 = self.driver.find_element_by_id("scriptcardtext").text
        print("quote-booking Script card : ", text_element18)
        assert '"Again, my name is venkatesh and I’m going to be here every step of the way to make sure this is the best move you’ve ever had.\n\nNow can I go ahead and get the address you\'re moving to and your email?"' in text_element18

        self.lf.clickonquotebookingSetforestimatorButton()
