import time

import pytest
from selenium import webdriver

import utilities
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
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class Test_001_Login:
    baseURL="https://wip.d1an3ax2xglzwd.amplifyapp.com"
    username="venki"
    password="Venki@123"
    searchCID="6988819"


    def test_homepageTitle(self,setup):
        #self.driver=webdriver.chrome()
        self.driver=setup
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title=self.driver.title


        if act_title == "CMS - All My Sons Moving and Storage":
            assert True
            self.driver.close()
            #self.logger.info("****** Home page tittle is passed: ******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            #self.logger.erroe("****** Home page title is failed ******")
            assert False

    def test_login(self,setup):
         #self.driver=webdriver.chrome()
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(10)
        self.lp=Login(self.driver)
        assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/login" in self.driver.current_url
        print(self.driver.current_url)
        time.sleep(10)
        self.lp.setUserName(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(5)
        assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/dashboard" in self.driver.current_url

        print(self.driver.current_url)
        #act_title = self.driver.title

        # act_title == "CMS - All My Sons Moving and Storage":
           #  assert True
             #self.driver.close()
            # self.logger.info("****** Login Pass test******")
        #else:
             #self.driver.save_screenshot(".\\Screenshots\\" + "LoginFailed.png")
            # self.driver.close()
            # self.logger.error("****** Login Failed test******")
             #assert False


        time.sleep(5)
        #self.lp.clickProfile()
        #time.sleep(3)
        #self.lp.clickLogout()
        #self.lp.clickSimulateLead()
        #time.sleep
        #time.sleep(2)
        #self.driver.switchTo().alert().sendKeys("123");
        #self.driver.switchTo().alert().accept();
        #assert "https://wip.d1an3ax2xglzwd.amplifyapp.com/login" in self.driver.current_url

        self.lp.clickSearchButton()
        time.sleep(5)
        self.lp.setSearchCID(self.searchCID)
        time.sleep(5)
        self.lp.clickSearchIcon()
        time.sleep(5)
        self.lp.clickSearchResult()





        #https://wip.d1an3ax2xglzwd.amplifyapp.com/login









