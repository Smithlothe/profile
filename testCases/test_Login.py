import pytest


from pageObject.LoginPage import loginpage
from utilities.readProperties import Readconfig
from utilities.Logger import LogGenerator

class Test_Login:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.sanity
    def test_Page_Title_001(self,setup):
        self.driver = setup
        self.log.info("test_Page_Title_001 is started")
        self.log.info("Openning Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this Url-->"+ self.Url)
        if self.driver.title == "OrangeHRM":
            assert True
            self.log.info("test_Page_Title_001 is Passed")
            self.log.info("Page Title is" + self.driver.title)
        else:
            assert False
            self.log.info("test_Page_Title_001 is Failed")

        self.driver.close()
        self.log.info("test_Page_Title_001 is Completed")


    def test_login_002(self,setup):
        self.driver=setup
        self.log.info("test_login_002 is Started")
        self.log.info("Openning Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this Url--> "+ self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering UserName--> "+ self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering Password--> " + self.password)
        self.lp.Click_Login()
        self.log.info("Click Login Button")
        if self.lp.Login_Status() == True:
            self.driver.save_screenshot("D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_login_002-pass.png")
            self.lp.Click_MenuButton()
            self.log.info("Click Menu Button")
            self.lp.Click_Logout()
            self.log.info("Click Logout Button")
            self.log.info("test_login_002 is passed")
            assert True
        else:
            self.log.info("test_login_002 is passed")
            self.driver.save_screenshot("D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_login_002-fail.png")
            assert False
        self.driver.close()
        self.log.info("test_login_002 is completed")