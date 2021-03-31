import pytest
import logging
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username =  ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("******** Test_001_Login *********")
        self.logger.info("******** Verifying Home Page Title *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        actualTitle =  self.driver.title

        if actualTitle == "OrangeHRM":
            assert True
            print(actualTitle)
            self.driver.close()
            self.logger.info("******** Home Page Title Test is Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("******** Home Page Title Test is Failed *********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("******** Verifying Login Test *********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        welcomeTitle=self.driver.title
        if welcomeTitle == "OrangeHRM":
            assert True
            print(welcomeTitle)
            self.logger.info("******** Home Page Title is Passed *********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("******** Home Page Title is Failed *********")
            assert False
