import pytest
from pageObject.AddEmp_Page import AddEmployee
from pageObject.LoginPage import loginpage
from utilities.readProperties import Readconfig
from utilities.Logger import LogGenerator
import time

class Test_Add_Emp:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.check
    def test_addEmp_003(self,setup):
        self.driver = setup
        self.log.info("test_addEmp_003 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to Url--> "+ self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter UserName --> "+ self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter Password --> "+ self.password)
        self.lp.Click_Login()
        self.log.info("Click on logIn")
        self.ae = AddEmployee(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click on PIM tab")
        self.ae.Click_AddEmployee()
        self.log.info("Click on Add Employee Button")
        self.ae.Enter_FirstName("justin")
        self.log.info("Enter Firstname --> Justin")
        self.ae.Enter_MiddleName("drake")
        self.log.info("Enter Middlename --> drake")
        self.ae.Enter_LastName("Beiber")
        self.log.info("Enter LastName --> Beiber")
        self.ae.Click_Save()
        self.log.info("Click on Save")
        if self.ae.Add_Employee_Status() == True:
            self.driver.save_screenshot("D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_addEmp_003_pass.png")
            self.lp.Click_MenuButton()
            self.log.info("Click on Menu Button")
            self.lp.Click_Logout()
            self.log.info("Click on LogOut")
            assert True
            self.log.info("test_addEmp_003 is passed")
        else:
            self.driver.save_screenshot(
                "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_addEmp_003_fail.png")
            self.log.info("test_addEmp_003 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_addEmp_003 is completed")

