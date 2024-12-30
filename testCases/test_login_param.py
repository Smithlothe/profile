import time

import pytest

from pageObject.LoginPage import loginpage
from utilities.readProperties import Readconfig
from utilities.Logger import LogGenerator

class Test_Login_Params:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.test
    def test_login_params_004(self, setup, getDataforlogin):
        self.driver = setup
        self.log.info("test_login_params_004 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.log.info("0 --> "+getDataforlogin[0])
        self.log.info("1 --> "+getDataforlogin[1])
        self.log.info("2 --> "+getDataforlogin[2])
        self.lp.Enter_UserName(getDataforlogin[0])
        self.log.info("Entering username-->" + getDataforlogin[0])
        self.lp.Enter_Password(getDataforlogin[1])
        self.log.info("Entering password-->" + getDataforlogin[1])
        self.lp.Click_Login()
        self.log.info("Click on login button")
        if self.lp.Login_Status() == True:
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot(
                    "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_login_params_004_pass.png")
                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")
                self.lp.Click_Logout()
                self.log.info("Click on logout button")
                self.log.info("test_login_002 is Passed")
                assert True
            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_login_params_004_fail.png")
                assert False
        else:
            if getDataforlogin[2] == "Fail":
                assert True
            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_login_params_004_fail1.png")
                assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")
