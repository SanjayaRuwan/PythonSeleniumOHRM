import time
import pytest
import logging
from pageObjects.LoginPage import LoginPage
from utilities import XLUtils
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig



class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginDataNew.xlsx"

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_ddt_login(self, setup):
        self.logger.info("******** Test_002_DDT_Login *********")
        self.logger.info("******** Verifying Login DDT Test *********")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        # Get row counts
        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number o f rows in a excel file", self.rows)

        # Empty  list variable
        list_status = []

        # Read excel file data
        for row in range(2, self.rows + 1):
            self.username = XLUtils.readData(self.path, 'Sheet1', row, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', row, 2)
            self.expResult = XLUtils.readData(self.path, 'Sheet1', row, 3)

            self.lp.setUserName(self.username)
            time.sleep(3)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            #self.lp.clickDashboard()
            #time.sleep(3)

            # act_title = self.driver.title
            # exp_title = "OrangeHRM"

            act_text=self.lp.visibleText()
            exp_text="Dashboard"

            if act_text == exp_text:
                if self.expResult == "Pass":
                    self.logger.info("Test Passed")
                    self.lp.clickLogout();
                    time.sleep(2)
                    self.lp.clickLogoutLink();
                    list_status.append("Pass")
                elif self.expResult == "Fail":
                    self.logger.info("Test Failed")
                    self.lp.clickLogout()
                    time.sleep(2)
                    self.lp.clickLogoutLink();
                    list_status.append("Fail")

            elif act_text != exp_text:
                if self.expResult == 'Pass':
                    self.logger.info("Test Failed")
                    list_status.append("Fail")
                elif self.expResult == 'Fail':
                    self.logger.info("Test Passed")
                    list_status.append("Pass")
            print(list_status)

        if "Fail" not in list_status:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False
