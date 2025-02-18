from Utils.locators import LoginPageElements
from Utils.locators import FormPageElements
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*LoginPageElements.USERNAME_TEXTBOX).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageElements.PASSWORD_TEXTBOX).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPageElements.LOGIN_BUTTON).click()
    

    def click_admin(self):
        self.driver.find_element(*FormPageElements.ADMIN_PANEL).click()

    def click_adduser(self):
        self.driver.find_element(*FormPageElements.ADD_USER).click()
    
    def click_user(self):
         self.driver.find_element(*FormPageElements.USER_DROP).click()
         dropdown = self.driver.find_element(*FormPageElements.USER_DROP) 
         dropdown.send_keys(Keys.DOWN)  
         dropdown.send_keys(Keys.ENTER)

    def enter_employee(self, employee):
        self.driver.find_element(*FormPageElements.EMPOLYEE_NAME).send_keys(employee)

    def click_status(self):
        self.driver.find_element(*FormPageElements.STATUS_DROP).click()
        dropdownstatus = self.driver.find_element(*FormPageElements.STATUS_DROP) 
        dropdownstatus.send_keys(Keys.DOWN)  
        dropdownstatus.send_keys(Keys.ENTER)

    def enter_username1(self, username1):
        self.driver.find_element(*FormPageElements.USERNAME_BOX).send_keys(username1)
    
    def enter_password1(self, password1):
        self.driver.find_element(*FormPageElements.PASSWORD_BOX).send_keys(password1)

    def enter_confrimpassword(self, confirmpassword):
        self.driver.find_element(*FormPageElements.CONFIRMPASSWORD_BOX).send_keys(confirmpassword)

    def click_save(self):
        self.driver.find_element(*FormPageElements.SAVE_BUTTON).click()

    def click_cancel(self):
        self.driver.find_element(*FormPageElements.CANCEL_BUTTON).click()
    

    def get_invalid_message(self):
     try:
        invalid_element = self.driver.find_element(*LoginPageElements.INVALID_CRED)
        return invalid_element.text if invalid_element else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None    

    def get_user_message(self):
     try:
        error_element = self.driver.find_element(*FormPageElements.USER_DROPERROR)
        return error_element.text if error_element else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None

    def get_employee_message(self):
     try:
        error_element1 = self.driver.find_element(*FormPageElements.EMPLOYEE_ERROR)
        return error_element1.text if error_element1 else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None


    def get_status_message(self):
     try:
        error_element2 = self.driver.find_element(*FormPageElements.STATUS_ERROR)
        return error_element2.text if error_element2 else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None


    def get_username_message(self):
     try:
        error_element3 = self.driver.find_element(*FormPageElements.USERNAME_ERROR)
        return error_element3.text if error_element3 else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None

    def get_passwordmissing_message(self):
     try:
        error_element5 = self.driver.find_element(*FormPageElements.PASSWORD_MISSING)
        return error_element5.text if error_element5 else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None

    def get_passwordnotmatch_message(self):
     try:
        error_element6 = self.driver.find_element(*FormPageElements.PASSWORD_NOTMATCH)
        return error_element6.text if error_element6 else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None