from selenium.webdriver.common.by import By

class EmployeeSearch:
    Text_EmpNameSearch_XPATH = (By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
    Click_SearchButton_XPATH = (By.XPATH,"//button[@type='submit']")
    SearchResult_CSSselector = (By.CSS_SELECTOR,"div[class='oxd-table-card'] div:nth-child(3) div:nth-child(1)")
    def __init__(self,driver):
        self.driver = driver

    def Enter_EmpName(self, empname):
        self.driver.find_element(*EmployeeSearch.Text_EmpNameSearch_XPATH).send_keys(empname)

    def Click_EmpSearch(self):
        self.driver.find_element(*EmployeeSearch.Click_SearchButton_XPATH).click()

    def EmpSearch_Result(self):
        search = self.driver.find_elements(*EmployeeSearch.SearchResult_CSSselector)
        search_len = len(search)
        if search_len == 0:
            return False
        elif search_len == 1:
            print(self.driver.find_element(*EmployeeSearch.SearchResult_CSSselector).text)
            return True