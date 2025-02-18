from selenium.webdriver.common.by import By

class LoginPageElements:

    USERNAME_TEXTBOX = (By.XPATH, "//input[@placeholder='Username']")
    PASSWORD_TEXTBOX = (By.XPATH, "//input[@placeholder='Password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@type,'submit')]")
    INVALID_CRED = (By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")


class FormPageElements:
     
     ADMIN_PANEL = (By.XPATH, "//*[@class='oxd-main-menu']/li[1]")
     ADD_USER = (By.XPATH, "//*[@class='orangehrm-paper-container']/div[1]/button")
     USER_DROP = (By.XPATH, "(//div[contains(text(),'-- Select --')])[1]")
     EMPOLYEE_NAME = (By.XPATH, "//input[@placeholder='Type for hints...']")
     STATUS_DROP = (By.XPATH,"//div[3]//div[1]//div[2]//div[1]//div[1]//div[1]")
     USERNAME_BOX = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
     PASSWORD_BOX = (By.XPATH, "(//input[@type='password'])[1]")
     CONFIRMPASSWORD_BOX = (By.XPATH, "(//input[@type='password'])[2]")
     SAVE_BUTTON = (By.XPATH, "//button[contains(@type,'submit')]")
     CANCEL_BUTTON = (By.XPATH, "//*[@class ='oxd-button oxd-button--medium oxd-button--ghost']")
     USER_DROPERROR = (By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required'])[1]")
     EMPLOYEE_ERROR = (By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required'])[2]")
     STATUS_ERROR = (By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required'])[3]")
     USERNAME_ERROR = (By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message'][normalize-space()='Required'])[4]")
     CONFIRM_ERROR = (By.XPATH,"//span[normalize-space()='Passwords do not match']")
     PASSWORD_MISSING = (By.XPATH,"//span[normalize-space()='Should have at least 7 characters']")
     PASSWORD_NOTMATCH = (By.XPATH, "//span[normalize-space()='Passwords do not match']")
      