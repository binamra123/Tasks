from selenium.webdriver.common.by import By

class LoginPageElements:

    USERNAME_TEXTBOX = (By.ID, "login-username")
    PASSWORD_TEXTBOX = (By.ID, "login-password")
    LOGIN_BUTTON = (By.XPATH, "//button[@id='login-button']")
    ERROR_MESSAGE = (By.XPATH, "//span[@class='Message-sc-15vkh7g-0 kGDZJw']")
    ERROR_USERNAME = (By.XPATH, "//span[contains(text(),'Please enter your Spotify username or email addres')]")
    ERROR_PASSWORD = (By.XPATH, "//span[normalize-space()='Please enter your password.']")
    PASSWORD_VISIBLE = (By.XPATH, "//*[name()='path' and contains(@d,'M22.207 2.')]")
    FORGOT_PASSWORD = (By.XPATH, "//p[@class='sc-czgmHJ kraIJY']")
    LOGIN_STATUS = (By.XPATH, "//span[text()='Web Player']")
    USER_DASHBOARD = (By.XPATH, "//a[@class='nmAHq8nfXRtoQmKU1gaF']//*[name()='svg']")
    RESET_PASSWORD = (By.XPATH, "//*[@class='encore-text encore-text-title-medium']")



