from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class LeadFlow:
    button_search_xpath = "//*[@id='Search']"
    button_searchtext_xpath = "//input[@id='txtSearch']"
    button_searchicon_xpath = "//body/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/*[1]"
    button_searchresult_xpath = "/html/body/div[2]/div[3]/div/div/div/div/div/div[2]/div/li/div[2]/div[1]"

    button_NewOpportunity_id = "NewOpportunity"

    textlabel_Customername_id = "custName"
    textlabel_cid_branch_id  = "cid"
    textlabel_callScriptcard_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/b[1]"

    textfield_Name_id = "name"
    textfield_PhoneNumber_id = "phone"
    button_name_phonepage_Continue_id = "btnCONTINUE"
    button_Yes_id = "Yes"
    button_No_id = "No"
    button_Yes_Continue_id = "btnCONTINUE"
    button_No_Continue_id = "btnCONTINUE"
    button_move_type_House_id = "House"
    button_move_type_Apartment_id = "Apartment"
    button_move_type_Condo_id = "Condo"
    button_move_type_Townhouse_id = "Townhouse"
    button_move_type_Office_id = "Office"
    button_move_type_Storage_id = "Storage"
    button_apartment_bedrooms_one_id = "1bedapartment"
    button_apartment_bedrooms_two_id = "2bedapartment"
    button_apartment_bedrooms_threeplus_id = "+3bedapartment"
    button_apartment_bedrooms_fewitems_id = "fewitems"
    testfield_fromAddres_id = "from"
    textfield_toAddress_id = "to"
    button_addstop_Address_id = "btnADDSTOP"
    textfield_addstop1_id = "addstop1"
    textfield_addstop2_id = "addstop2"
    textfield_addstop3_id = "addstop3"
    button_delete_addstop1_id = "icoaddstop1"
    button_delete_addstop2_id = "icoaddstop2"
    button_delete_addstop3_id = "icoaddstop3"
    button_addresspage_Continue_id = "btnCONTINUE"
    button_apartment_from_floors_1st_id = "1st"
    button_apartment_from_floors_2nd_id = "2nd"
    button_apartment_from_floors_3rd_id = "3rd"
    button_apartment_from_floors_4th_id = "4th"
    button_apartment_from_floors_Higher_id = "Higher"
    button_apartment_to_floors_1st_id = "1st"
    button_apartment_to_floors_2nd_id = "2nd"
    button_apartment_to_floors_3rd_id = "3rd"
    button_apartment_to_floors_4th_id = "4th"
    button_apartment_to_floors_Higher_id = "Higher"
    button_floors_Continue_id = "btnCONTINUE"
    button_VerifyHouseInfo_Continue_id ="btnCONTINUE"
    button_entire_move_YesEntireHome_id = "YesEntireHome"
    button_entire_move_NoPartialMove_id = "NoPartialMove"
    button_entire_move_NoaFewItems_id = "NoaFewItems"
    button_move_date_EXACTDATE_id = "btnEXACTDATE"
    button_move_date_FLEXIBLEDATE_id = "btnFLEXIBLEDATE"
    button_special_reqs_1_id = ""
    button_special_reqs_2_id = ""
    button_special_reqs_Continue_id = "btnCONTINUE"
    textfield_heaviest_item_id = "heaviest"
    button_heaviest_item_Continue_id = "btnCONTINUE"
    button_packing_Wepackitforyou_id = "Wepackitforyou"
    button_packing_SelfPacking_id = "SelfPacking"

    button_last_move_Continue_id = "btnCONTINUE"
    button_Thankyou_Continue_id = "btnCONTINUE"

    button_pricing_2movers_id = "2Movers"
    button_pricing_3movers_id = "3Movers"
    button_pricing_4movers_id = "4 Movers"
    button_pricing_Continue_id = "btnCONTINUE"

    button_quote_booking_setforestimator_id = "setforestimator"

    # button_quote_booking_setforestimator_id = "setforestimator"
    # button_quote_booking_setforestimator_id = "setforestimator"

    def __init__(self, driver):
        self.driver = driver

    #def getElement(self, elementId):
        #return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((by.id,by.xpath, elementId)))

    def clickSearchButton(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()

    def setSearchCID(self, searchCID):
        self.driver.find_element_by_xpath(self.button_searchtext_xpath).clear()
        self.driver.find_element_by_xpath(self.button_searchtext_xpath).send_keys(searchCID)

    def clickSearchIcon(self):
        self.driver.find_element_by_xpath(self.button_searchicon_xpath).click()

    def clickSearchResult(self):
        self.driver.find_element_by_xpath(self.button_searchresult_xpath).click()

    def clickNewOpportunity(self):
        self.driver.find_element_by_id(self.button_NewOpportunity_id).click()


    def getcidandbranch(self):
            self.driver.find_element_by_id(self.textlabel_cid_branch_id).getText()


        #textlabel_callScriptcard_xpath = "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/b[1]"

    def setCustomerName(self, name):
        self.driver.find_element_by_id(self.textfield_Name_id).clear()
        self.driver.find_element_by_id(self.textfield_Name_id).send_keys(name)

    def setCustomerPhone(self, phone):
        self.driver.find_element_by_id(self.textfield_PhoneNumber_id).clear()
        self.driver.find_element_by_id(self.textfield_PhoneNumber_id).send_keys(phone)

    def clickNameandPhonepageContinueButton(self):
        self.driver.find_element_by_id(self.button_name_phonepage_Continue_id).click()

    def clickYesButton(self):
        self.driver.find_element_by_id(self.button_Yes_id).click()

    def clickNoButton(self):
        self.driver.find_element_by_id(self.button_No_id).click()

    def clickYesContinueButton(self):
        self.driver.find_element_by_id(self.button_Yes_Continue_id).click()

    def clickNoContinueButton(self):
        self.driver.find_element_by_id(self.button_No_Continue_id).click()

    def clickOnHouse(self):
        self.driver.find_element_by_id(self.button_move_type_House_id).click()

    def clickOnApartment(self):
        self.driver.find_element_by_id(self.button_move_type_Apartment_id).click()

    def clickOnCondo(self):
        self.driver.find_element_by_id(self.button_move_type_Condo_id).click()

    def clickOnTownhouse(self):
        self.driver.find_element_by_id(self.button_move_type_Townhouse_id).click()

    def clickOnOffice(self):
        self.driver.find_element_by_id(self.button_move_type_Office_id).click()

    def clickonStorage(self):
        self.driver.find_element_by_id(self.button_move_type_Storage_id).click()

    def clickon1bedapartment(self):
        self.driver.find_element_by_id(self.button_apartment_bedrooms_one_id).click()

    def clickon2bedapartment(self):
        self.driver.find_element_by_id(self.button_apartment_bedrooms_two_id).click()

    def clickonplus3bedapartment(self):
        self.driver.find_element_by_id(self.button_apartment_bedrooms_threeplus_id).click()

    def clickonfewitems(self):
        self.driver.find_element_by_id(self.button_apartment_bedrooms_fewitems_id).click()

    def setFromAddress(self, fromAddress):
        self.driver.find_element_by_id(self.testfield_fromAddres_id).clear()
        self.driver.find_element_by_id(self.testfield_fromAddres_id).send_keys(fromAddress)

    def setToAddress(self, toAddress):
        self.driver.find_element_by_id(self.textfield_toAddress_id).clear()
        self.driver.find_element_by_id(self.textfield_toAddress_id).send_keys(toAddress)

    def clickonAddStop(self):
        self.driver.find_element_by_id(self.button_addstop_Address_id).click()

    def setAddstop1Address(self,addaddres1):
        self.driver.find_element_by_id(self.textfield_addstop1_id).clear()
        self.driver.find_element_by_id(self.textfield_addstop1_id).send_keys(addaddres1)

    def setAddstop2Address(self,addaddress2):
        self.driver.find_element_by_id(self.textfield_addstop2_id).clear()
        self.driver.find_element_by_id(self.textfield_addstop2_id).send_keys(addaddress2)

    def setAddstop3Address(self,addaddress3):
        self.driver.find_element_by_id(self.textfield_addstop3_id).clear()
        self.driver.find_element_by_id(self.textfield_addstop3_id).send_keys(addaddress3)

    def clickonDeleteAddStop1(self):
        self.driver.find_element_by_id(self.button_delete_addstop1_id).click()

    def clickonDeleteAddStop2(self):
        self.driver.find_element_by_id(self.button_delete_addstop2_id).click()

    def clickonDeleteAddStop3(self):
        self.driver.find_element_by_id(self. button_delete_addstop3_id).click()

    def clickonAddresspageContinueButton(self):
        self.driver.find_element_by_id(self.button_addresspage_Continue_id).click()

    def clickonFromApptFloors1(self):
        self.driver.find_element_by_id(self.button_apartment_from_floors_1st_id).click()

    def clickonFromApptFloors2(self):
        self.driver.find_element_by_id(self.button_apartment_from_floors_2nd_id) .click()

    def clickonFromApptFloors3(self):
        self.driver.find_element_by_id(self.button_apartment_from_floors_3rd_id).click()

    def clickonFromApptFloors4(self):
        self.driver.find_element_by_id(self.button_apartment_from_floors_4th_id).click()

    def clickonFromApptFloorsHigher(self):
        self.driver.find_element_by_id(self.button_apartment_from_floors_Higher_id).click()

    def clickontoApptFloors1(self):
        self.driver.find_element_by_id(self.button_apartment_to_floors_1st_id) .click()

    def clickOntoApptFloors2(self):
        self.driver.find_element_by_id(self.button_apartment_to_floors_2nd_id ).click()

    def clickontoApptFloors3(self):
        self.driver.find_element_by_id(self.button_apartment_to_floors_3rd_id).click()

    def clickontoApptFloors4(self):
        self.driver.find_element_by_id(self.button_apartment_to_floors_4th_id) .click()

    def clickontoApptFloorsHigher(self):
        self.driver.find_element_by_id(self. button_apartment_to_floors_Higher_id).click()

    def clickonFloorspageContinuebutton(self):
        self.driver.find_element_by_id(self.button_floors_Continue_id).click()

    def clickonVerifyHouseButton(self):
        self.driver.find_element_by_id(self.button_VerifyHouseInfo_Continue_id).click()

    def clickonYesEntireHome(self):
        self.driver.find_element_by_id(self.button_entire_move_YesEntireHome_id) .click()

    def clickonNoPartialMove(self):
        self.driver.find_element_by_id(self. button_entire_move_NoPartialMove_id).click()

    def clickonNoaFewItems(self):
        self.driver.find_element_by_id(self.button_entire_move_NoaFewItems_id).click()

    def clickonExactdate(self):
        self.driver.find_element_by_id(self.button_move_date_EXACTDATE_id) .click()

    def clickonFlexibledate(self):
        self.driver.find_element_by_id(self. button_move_date_FLEXIBLEDATE_id).click()

    def clickonSpecialReqsContinueButton(self):
        self.driver.find_element_by_id(self.button_special_reqs_Continue_id).click()

    def clickonHeaviest(self,heaviitem):
        self.driver.find_element_by_id(self.textfield_heaviest_item_id).clear()
        self.driver.find_element_by_id(self.textfield_heaviest_item_id).send_keys(heaviitem)

    def clickonHeaviestpageContinueButton(self):
        self.driver.find_element_by_id(self.button_heaviest_item_Continue_id) .click()

    def clickonWepackitforyou(self):
        self.driver.find_element_by_id(self.button_packing_Wepackitforyou_id).click()

    def clickonSelfPacking(self):
        self.driver.find_element_by_id(self.button_packing_SelfPacking_id).click()

    def clickonlastmoveContinueButton(self):
        self.driver.find_element_by_id(self.button_last_move_Continue_id) .click()

    def clickonThankyoupageContinuebutton(self):
        self.driver.find_element_by_id(self.button_Thankyou_Continue_id).click()

    def clickontwoMovers(self):
        self.driver.find_element_by_id(self.button_pricing_2movers_id).click()

    def clickonthreeMovers(self):
        self.driver.find_element_by_id(self.button_pricing_3movers_id).click()

    def clickonfourMovers(self):
        self.driver.find_element_by_id(self.button_pricing_4movers_id).click()

    def clickonpricingContinueButton(self):
        self.driver.find_element_by_id(self.button_pricing_Continue_id).click()

    def clickonquotebookingSetforestimatorButton(self):
        self.driver.find_element_by_id(self.button_quote_booking_setforestimator_id).click()








