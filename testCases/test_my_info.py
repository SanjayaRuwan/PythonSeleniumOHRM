import time
import logging
from pageObjects.MyInfoPage import MyInfo
from testCases.test_login import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_002_GenInfo:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger1 = LogGen.loggen()


    def test_gotoMyInfo(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger1.info("***** Login success *****")

        self.minfo = MyInfo(self.driver)
        time.sleep(2)
        self.minfo.clickMyInfo()
        self.logger1.info("***** My Info Page *****")
        time.sleep(2)
        self.minfo.clickEdit()
        time.sleep(2)
        self.minfo.setFName("Sanjaya")
        self.minfo.setMName("Ruwan")
        self.minfo.setLName("Kumara")
        self.minfo.setLicenseNo("98275845896")
        self.minfo.setLicenseExpDate("2021-08-31")
        self.minfo.selectGender()
        self.minfo.selectMarital("Single")
        self.minfo.clickSave()
        self.logger1.info("***** My Info Data Updated Successfully *****")
        time.sleep(5)

        self.driver.close()
