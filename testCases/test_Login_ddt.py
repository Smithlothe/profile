import pytest

from pageObject.LoginPage import loginpage
from utilities import XLutils
from utilities.Logger import LogGenerator
from utilities.readProperties import Readconfig

class Test_Login_DDT:
    Url = Readconfig.geturl()
    log = LogGenerator.loggen()
    path = "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\TestData\\LoginData.xlsx"


    @pytest.mark.notdone
    def test_login_ddt_006(self,setup):
        self.driver = setup
        self.log.info("test_login_ddt_006 is started...")
        self.log.info("Openning Browser")
        self.driver.get(self.Url)
        self.log.info("get to this Url --> "+self.Url)
        self.lp = loginpage(self.driver)
        self.rows = XLutils.getrowCount(self.path,"Sheet1")
        login_status = []
        for r in range(2,self.rows+1):
            self.username = XLutils.readData(self.path,"Sheet1",r,2)
            self.password = XLutils.readData(self.path,"Sheet1",r,3)
            self.lp.Enter_UserName(self.username)
            self.log.info("Entering Username --> "+self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Entering Password --> "+self.password)
            self.lp.Click_Login()

            if self.lp.Login_Status() == True:
                self.driver.save_screenshot("D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_login_ddt_006-pass.png")
                self.lp.Click_MenuButton()
                self.log.info("Clicking on menu button")
                self.lp.Click_Logout()
                self.log.info("Click on Logout Button")
                login_status.append("Pass")
                XLutils.writeData(self.path,"Sheet1",r,4,"Pass")
            else:
                login_status.append("Fail")
                XLutils.writeData(self.path,"Sheet1",r,4,"Fail")
                self.driver.save_screenshot("D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\"+self.username+self.password+"test_login_ddt_006-fail.png")

        if "Pass" in login_status:
            self.log.info("test_login_ddt_006 is Passed")
            assert True
        else:
            self.log.info("test_login_ddt_006 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_login_ddt_006 is completed")


