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
        self.driver.implicitly_wait(10)  # seconds
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
        self.minfo.clickEdit()
        time.sleep(2)
        self.minfo.setFName("Sanjaya")
        self.minfo.setMName("Ruwan")
        self.minfo.setLName("Kumara")
        self.minfo.setLicenseNo("98275845896")
        self.minfo.setLicenseExpDate("2021-08-31")
        self.minfo.selectGender()
        self.minfo.selectMarital("Single")
        self.minfo.selectNatinality("Sri Lankan")
        self.minfo.clickSave()
        self.logger1.info("***** My Info Personal Data Updated Successfully *****")
        time.sleep(3)

        self.minfo.clickBloodSave()
        self.minfo.selectblood("AB+")
        self.minfo.clickBloodSave()
        time.sleep(2)
        self.logger1.info("***** My Blood Details Updated Successfully *****")

        self.minfo.clickContact()
        self.minfo.clickEdit()
        self.minfo.setAddress1("Colombo")
        self.minfo.setAddress2("Kandy")
        self.minfo.setCity("Colombo")
        self.minfo.setZip("834753")
        self.minfo.setMobile("0712485345")
        self.minfo.setEmail("san@ohrm.com")
        self.minfo.clickEdit()
        time.sleep(2)
        self.logger1.info("***** My Contact Details Updated Successfully *****")

        self.driver.close()
