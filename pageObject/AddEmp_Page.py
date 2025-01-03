from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as Ec

class AddEmployee:
    Click_PIM_XPATH = (By.XPATH,"//span[normalize-space()='PIM']")
    Click_AddEmployee_XPATH = (By.XPATH,"//a[normalize-space()='Add Employee']")
    Text_FirstName_XPATH = (By.XPATH,"//input[@placeholder='First Name']")
    Text_MiddleName_XPATH = (By.XPATH,"//input[@placeholder='Middle Name']")
    Text_LastName_XPATH = (By.XPATH,"//input[@placeholder='Last Name']")
    Click_Save_XPATH = (By.XPATH,"//button[@type='submit']")
    PersonalDetail_Tab_XPATH = (By.XPATH,"//h6[normalize-space()='Personal Details']")

    def __init__(self,driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*AddEmployee.Click_PIM_XPATH).click()

    def Click_AddEmployee(self):
        self.driver.find_element(*AddEmployee.Click_AddEmployee_XPATH).click()

    def Enter_FirstName(self, firstname):
        self.driver.find_element(*AddEmployee.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_MiddleName(self, middlename):
        self.driver.find_element(*AddEmployee.Text_MiddleName_XPATH).send_keys(middlename)

    def Enter_LastName(self, lastname):
        self.driver.find_element(*AddEmployee.Text_LastName_XPATH).send_keys(lastname)

    def Click_Save(self):
        self.driver.find_element(*AddEmployee.Click_Save_XPATH).click()

    def Add_Employee_Status(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*AddEmployee.PersonalDetail_Tab_XPATH)
            return True
        except Ec:
            return False
