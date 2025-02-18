from Utils.locators import LoginPageElements
from selenium.webdriver.common.action_chains import ActionChains


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*LoginPageElements.USERNAME_TEXTBOX).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPageElements.PASSWORD_TEXTBOX).send_keys(password)

    def text_username(self):
        email_field= self.driver.find_element(*LoginPageElements.USERNAME_TEXTBOX)
        return email_field

    def text_password(self):
        password_field= self.driver.find_element(*LoginPageElements.PASSWORD_TEXTBOX)
        return password_field

    def click_login(self):
        self.driver.find_element(*LoginPageElements.LOGIN_BUTTON).click()

    def click_forgotpass(self):
        self.driver.find_element(*LoginPageElements.FORGOT_PASSWORD).click()

    def click_passwordvisible(self):
        self.driver.find_element(*LoginPageElements.PASSWORD_VISIBLE).click()
    
    def click_loginstatus(self):
        self.driver.find_element(*LoginPageElements.LOGIN_STATUS).click()
    
    def click_dashboard(self):
        self.driver.find_element(*LoginPageElements.USER_DASHBOARD).click()

    def page_resetpassword(self):
        resetpassword_page= self.driver.find_element(*LoginPageElements.RESET_PASSWORD)
        return resetpassword_page.text


    def get_error_message(self):
     try:
        error_element = self.driver.find_element(*LoginPageElements.ERROR_MESSAGE)
        return error_element.text if error_element else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None

    def get_error_username(self):
     try:
        error_element1 = self.driver.find_element(*LoginPageElements.ERROR_USERNAME)
        return error_element1.text if error_element1 else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None
    
    
    def get_error_password(self):
     try:
        error_element2 = self.driver.find_element(*LoginPageElements.ERROR_PASSWORD)
        return error_element2.text if error_element2 else None
     except Exception as e:
        print(f"An error occurred while getting the error message: {e}")
        return None








    

    

    