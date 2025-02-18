import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#  TC_001 - Verify logging into the application.
def test_login(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    WebDriverWait(setup, 10).until(EC.url_contains("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"))
    assert setup.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

#  TC_002 - Verify logging into the application using invalid credentials.(invalid error validation.)
def test_invaliderror(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin")
    form_page.click_login()
    invalid_message = form_page.get_invalid_message()
    expected_invalid_message = "Invalid credentials"
    assert invalid_message == expected_invalid_message

#  TC_003 - Verify logging into the application and filling up the form.
def test_fillform(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.click_user()
    form_page.enter_employee("Orange  Test")
    form_page.click_status()
    form_page.enter_username1("Test Username")
    form_page.enter_password1("@Password@123")
    form_page.enter_confrimpassword("@Password@123")


#  TC_004 - Verify logging without filling forms.
def test_blankform(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.click_save()
   
#  TC_005 - Validate error for User Role
def test_usererror(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.enter_employee("Charles  Carter")
    form_page.click_status()
    form_page.enter_username1("Test Username")
    form_page.enter_password1("@Password@123")
    form_page.enter_confrimpassword("@Password@123")
    form_page.click_save()
    user_message = form_page.get_user_message()
    expected_user_message = "Required"
    assert user_message == expected_user_message


#  TC_006 - Validate error for Employee
def test_employeeerror(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.click_user()
    form_page.click_status()
    form_page.enter_username1("Test Username")
    form_page.enter_password1("@Password@123")
    form_page.enter_confrimpassword("@Password@123")
    form_page.click_save()
    employee_message = form_page.get_user_message()
    expected_employee_message = "Required"
    assert employee_message == expected_employee_message


#  TC_007 - Validate error for Status
def test_statuserror(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.click_user()
    form_page.enter_employee("Charles  Carter") 
    form_page.enter_username1("Test Username")
    form_page.enter_password1("@Password@123")
    form_page.enter_confrimpassword("@Password@123")
    form_page.click_save()
    status_message = form_page.get_status_message()
    expected_status_message = "Required"
    assert status_message == expected_status_message


#  TC_008 - Validate error for Username
def test_usernameerror(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.click_user()
    form_page.enter_employee("Charles  Carter") 
    form_page.click_status()
    form_page.enter_password1("@Password@123")
    form_page.enter_confrimpassword("@Password@123")
    form_page.click_save()
    username_message = form_page.get_username_message()
    expected_username_message = "Required"
    assert username_message == expected_username_message

#  TC_009 - Validate error for Password (Unvalid Password)
def test_passworderror(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.click_user()
    form_page.enter_employee("Charles  Carter") 
    form_page.click_status()
    form_page.enter_username1("Test Username")
    form_page.enter_password1("abcdef")
    form_page.enter_confrimpassword("abcedf")
    form_page.click_save()
    password_message = form_page.get_passwordmissing_message()
    expected_password_message = "Should have at least 7 characters"
    assert password_message == expected_password_message


#  TC_010 - Validate error for ConfirmPassword
def test_confirmpassworderror(form_page, setup):
    form_page.enter_username("Admin")
    form_page.enter_password("admin123")
    form_page.click_login()
    form_page.click_admin()
    form_page.click_adduser()
    form_page.click_user()
    form_page.enter_employee("Charles  Carter") 
    form_page.click_status()
    form_page.enter_username1("Test Username")
    form_page.enter_password1("@Password@123")
    form_page.enter_confrimpassword("abcedf")
    form_page.click_save()
    confirmpassword_message = form_page.get_passwordnotmatch_message()
    expected_confirmpassword_message = "Passwords do not match"
    assert confirmpassword_message == expected_confirmpassword_message