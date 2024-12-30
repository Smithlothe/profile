import pytest
import time
from pageObject.LoginPage import loginpage
from pageObject.AddEmp_Page import AddEmployee
from pageObject.EmpSearchPage import EmployeeSearch
from utilities.readProperties import Readconfig
from utilities.Logger import LogGenerator

class Test_Emp_Search:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.search
    def test_SearchEmp_005(self,setup):
        self.driver = setup
        self.log.info("test_searchEmp_005 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to Url--> " + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter UserName --> " + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter Password --> " + self.password)
        self.lp.Click_Login()
        self.log.info("Click on logIn")
        self.ae = AddEmployee(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click on PIM tab")
        self.es = EmployeeSearch(self.driver)
        self.es.Enter_EmpName("Justin")
        self.log.info("Enter EmpName for Search --> Justin")
        self.es.Click_EmpSearch()
        self.log.info("Click on Search Button")
        time.sleep(5)
        if self.es.EmpSearch_Result() == True:
            self.log.info("Search Found")
            self.log.info("test_SearchEmp_005 is Passed")
            self.lp.Click_MenuButton()
            self.log.info("Click on Menu Button")
            self.lp.Click_Logout()
            self.log.info("Click on LogOut")
            assert True
        else:
            self.log.info("test_SearchEmp_005 is Failed")
            assert False

        self.driver.close()
        self.log.info("test_SearchEmp_005 is Completed")


