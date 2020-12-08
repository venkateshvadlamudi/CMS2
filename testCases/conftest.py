from telnetlib import EC

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def setup():
    #driver =webdriver.Chrome(executable_path=".//TestData/chromedriver.exe")
    #return driver
    timeout = 15
    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver



"""
 @pytest.fixture()
def setup(browser):
    if browser=='chrome':
       driver =webdriver.Chrome(executable_path="D:\chromedriver.exe")
    elif browser == 'firefox':
        driver=webdriver.Firefox
    elif browser == 'ie':
        driver=webdriver.Ie
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
     """
##### pyTest HTML Reports ######

# It is Hook for Adding Environment info to HTML Reports

def pytest_configure(config):
    config._metadata['project name']='CMS'
    config._metadata[' Module name'] = 'Login'
    config._metadata['project name'] = 'Venkatesh'

# It is hook for delete/Modify Environment info HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME" , None)
    metadata.pop("Plugins", None)