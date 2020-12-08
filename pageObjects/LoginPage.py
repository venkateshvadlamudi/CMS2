from selenium import webdriver
from selenium.webdriver import ActionChains


class Login:
    textbox_username_id="username"
    textbox_password_id="password"
    button_login_id="btnLOGIN"
    button_userprofile_id="userProfile"
    button_logout_id="btnLOGOUT"


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

