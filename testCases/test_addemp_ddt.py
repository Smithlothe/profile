import time

import pytest

from pageObject.LoginPage import loginpage
from pageObject.AddEmp_Page import AddEmployee
from utilities.Logger import LogGenerator
from utilities.readProperties import Readconfig
from utilities import XLutils

class Test_addEmp_DDT:

    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\TestData\\EmployeeList.xlsx"

    @pytest.mark.addempddt
    def test_addEmp_ddt_007(self,setup):
        self.driver = setup
        self.log.info("test_addEmp_ddt_007 is Started")
        self.log.info("Browser is openning")
        self.driver.get(self.Url)
        self.log.info("Go to Url--> "+self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering Username "+ self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password " +self.password)
        self.lp.Click_Login()
        self.log.info("Click on Login Button")
        self.ae = AddEmployee(self.driver)
        self.ae.Click_PIM()
        self.log.info("CLick on PIM")
        self.rows = XLutils.getrowCount(self.path,"Sheet1")
        self.ae.Click_AddEmployee()
        self.log.info("Click on Add Employee Button")
        status_list = []
        for r in range(2,self.rows+1):
            self.firstname = XLutils.readData(self.path,"Sheet1",r,2)
            self.middlename = XLutils.readData(self.path,"Sheet1",r,3)
            self.lastname = XLutils.readData(self.path,"Sheet1",r,4)
            self.ae.Enter_FirstName(self.firstname)
            self.log.info("Entering FirstName -->"+self.firstname)
            self.ae.Enter_MiddleName(self.middlename)
            self.log.info("Entering middlename -->"+self.middlename)
            self.ae.Enter_LastName(self.lastname)
            self.log.info("Entering Lastname -->"+self.lastname)
            self.ae.Click_Save()
            self.log.info("Click Save Button")
            if self.ae.Add_Employee_Status() == True:
                self.ae.Click_AddEmployee()
                self.log.info("Clik Add EMp Button")
                status_list.append("Pass")
                XLutils.writeData(self.path,"Sheet1",r,5,"Pass")
                self.driver.save_screenshot("D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_addEmp_ddt_007-pass.png")
            else:
                status_list.append("Fail")
                XLutils.writeData(self.path,"Sheet1",r,5,"Fail")
                self.driver.save_screenshot(
                    "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_addEmp_ddt_007-fail.png")

        time.sleep(2)
        self.lp.Click_MenuButton()
        self.log.info("Click Menu Button")
        self.lp.Click_Logout()
        self.log.info("Click Logout Button")

        if "Fail" not in status_list:
            self.log.info("test_addEmp_ddt_007 is Passed")
            assert True
        else:
            self.log.info("test_addEmp_ddt_007 is Failed")
            assert False

        self.log.info("test_addEmp_ddt_007 is Completed")