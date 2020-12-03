from selenium import webdriver
from selenium.webdriver import ActionChains


class Login:
    textbox_username_id="username"
    textbox_password_id="password"
    button_login_id="btnLOGIN"
    button_userprofile_id="userProfile"
    button_logout_id="btnLOGOUT"
    #button_simulatelead_cssSelector="div.jss35 div.jss51 div.jss52:nth-child(1) div.jss46 div.jss55 ul:nth-child(1) li:nth-child(3) > button.MuiButtonBase-root-281.MuiFab-root-273.jss261.jss262.jss271.MuiFab-extended-277"
    button_search_xpath="//*[@id='Search']"
    button_searchtext_xpath = "//input[@id='txtSearch']"
    button_searchicon_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/*[1]"
    button_searchresult_xpath = "/html/body/div[2]/div[3]/div/div/div/div/div/div[2]/div/li/div[2]/div[1]"



    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_id(self.button_login_id).click()

    def clickProfile(self):
        self.driver.find_element_by_id(self.button_userprofile_id).click()

    def clickLogout(self):
        self.driver.find_element_by_id(self.button_logout_id).click()

    #def clickSimulateLead(self):
        #actions = ActionChains(self.driver)
        #actions.click(self.driver.find_element_by_css_selector(self.button_simulatelead_cssSelector).click())
        # perform the operation on the element
       # actions.perform()
        #alert = self.driver.switch_to.alert
        #alert.sendKeys("123");
        #alert().accept();

    def clickSearchButton(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()

    def setSearchCID(self,searchCID):
        self.driver.find_element_by_xpath(self.button_searchtext_xpath).clear()
        self.driver.find_element_by_xpath(self.button_searchtext_xpath).send_keys(searchCID)

    def clickSearchIcon(self):
        self.driver.find_element_by_xpath(self.button_searchicon_xpath).click()

    def clickSearchResult(self):
        self.driver.find_element_by_xpath(self.button_searchresult_xpath).click()


        #self.driver.find_element_by_css_selector(self.button_simulatelead_cssSelector).click()