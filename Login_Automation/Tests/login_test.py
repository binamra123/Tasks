import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


#  TC_001 - Verify logging into the application using valid credentials.(i.e valid email and password)
def test_validemail(login_page, setup):
    login_page.enter_username("binamraacharya582@gmail.com")
    login_page.enter_password("Spotify@123")
    login_page.click_login()
    login_page.click_loginstatus()
    WebDriverWait(setup, 10).until(EC.url_contains("https://open.spotify.com/"))
    assert setup.current_url == "https://open.spotify.com/"

#  TC_002 - Verify logging into the application using valid credentials.(i.e valid username and password)
def test_validusername(login_page, setup):
    login_page.enter_username("wo85bak39je1f70xv166sncle")
    login_page.enter_password("Spotify@123")
    login_page.click_login()
    login_page.click_loginstatus()
    WebDriverWait(setup, 10).until(EC.url_contains("https://open.spotify.com/"))
    assert setup.current_url == "https://open.spotify.com/"

#  TC_003 - Verify logging into the application using invalid credentials. (i.e invalid 'email'and invalid 'password')
def test_invalidemail(login_page, setup):
    login_page.enter_username("binamraacharya582@abcd.com")
    login_page.enter_password("abcd@123")
    login_page.click_login()
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect username or password."
    assert error_message == expected_error_message


#  TC_004 - Verify logging into the application using invalid credentials. (i.e invalid 'username' and invalid 'password')
def test_invalidusername(login_page, setup):
    login_page.enter_username("abcdefgh")
    login_page.enter_password("xyz@123")
    login_page.click_login()
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect username or password."
    assert error_message == expected_error_message

#  TC_005 - Verify logging into the application using valid email and invalid password credentials
def test_invalidpassword1(login_page, setup):
    login_page.enter_username("binamraacharya582@gmail.com")
    login_page.enter_password("abcd@1234")
    login_page.click_login()
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect username or password."
    assert error_message == expected_error_message

#  TC_006 - Verify logging into the application using valid username and invalid password credentials
def test_invalidpassword2(login_page, setup):
    login_page.enter_username("wo85bak39je1f70xv166sncle")
    login_page.enter_password("abcd@123")
    login_page.click_login()
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect username or password."
    assert error_message == expected_error_message

#  TC_007 - Verify logging into the application using invalid email and valid password credentials
def test_invalidemail1(login_page, setup):
    login_page.enter_username("binamraacharya@.com")
    login_page.enter_password("Spotify@123")
    login_page.click_login()
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect username or password."
    assert error_message == expected_error_message

#  TC_008 - Verify logging into the application using invalid username and valid password credentials
def test_invalidusername1(login_page, setup):
    login_page.enter_username("abcdefgh")
    login_page.enter_password("Spotify@123")
    login_page.click_login()
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect username or password."
    assert error_message == expected_error_message

#  TC_009 - Verify logging into the application without providing any credentials
def test_blankcredentials(login_page, setup):
    login_page.enter_username("")
    login_page.enter_password("")
    login_page.click_login()
    email_error_message = login_page.get_error_username()
    expected_error_message1 = "Please enter your Spotify username or email address."
    password_error_message = login_page.get_error_password()
    expected_error_message2 = "Please enter your password."
    assert email_error_message == expected_error_message1
    assert password_error_message == expected_error_message2


#  TC_010 - Verify logging into the application using valid email and blank password.
def test_blankpassword1(login_page, setup):
    login_page.enter_username("binamraacharya582@gmail.com")
    login_page.enter_password("")
    login_page.click_login()
    password_error_message = login_page.get_error_password()
    expected_error_message = "Please enter your password."
    assert password_error_message == expected_error_message


#  TC_011 - Verify logging into the application using valid username and blank password.
def test_blankpassword2(login_page, setup):
    login_page.enter_username("wo85bak39je1f70xv166sncle")
    login_page.enter_password("")
    login_page.click_login()
    password_error_message = login_page.get_error_password()
    expected_error_message = "Please enter your password."
    assert password_error_message == expected_error_message

#  TC_012 - Verify logging into the application using blank email and valid password.
def test_blankemail(login_page, setup):
    login_page.enter_username("")
    login_page.enter_password("Spotify@123")
    login_page.click_login()
    email_error_message = login_page.get_error_username()
    expected_error_message = "Please enter your Spotify username or email address."
    assert email_error_message == expected_error_message

#  TC_013 - Verify logging into the application using blank username and valid password.
def test_blankusername(login_page, setup):
    login_page.enter_username("")
    login_page.enter_password("Spotify@123")
    login_page.click_login()
    email_error_message = login_page.get_error_username()
    expected_error_message = "Please enter your Spotify username or email address."
    assert email_error_message == expected_error_message

#  TC_014 - Verify that the 'Email or username' and 'Password' field has proper placeholder text.
def test_placeholder(login_page, setup):
    email_placeholder = login_page.text_username()
    password_placeholder = login_page.text_password()
    placeholder_email = email_placeholder.get_attribute("placeholder")
    placeholder_password = password_placeholder.get_attribute("placeholder")
    expected_placeholderemail = "Email or username"
    expected_placeholderpassword = "Password"
    assert placeholder_email == expected_placeholderemail
    assert placeholder_password == expected_placeholderpassword

#  TC_015 - Verify that the password entered in 'Password' text field is made not to be visible.
def test_passwordtype(login_page, setup):
    password_visible = login_page.text_password()
    visible_password = password_visible.get_attribute("type")
    expected_passwordtype = "password"
    assert visible_password == expected_passwordtype

#  TC_016 - Verify the view password icon in the 'Password' text field.
def test_passwordvisibile(login_page, setup):
    login_page.enter_username("binamraacharya582@gmail.com")
    login_page.enter_password("Spotify@123")
    login_page.click_passwordvisible()
    password_visible = login_page.text_password()
    visible_password = password_visible.get_attribute("type")
    expected_passwordtype = "text"
    assert visible_password == expected_passwordtype


#  TC_017 - Verify the view password icon in the 'Password' text field is disabled by default.
def test_passwordicon(login_page, setup):
    password_icon = login_page.text_password()
    icon_password = password_icon.get_attribute("type")
    expected_passwordicon = "password"
    assert icon_password == expected_passwordicon

#  TC_018 - Verify the copying of the password entered in 'Password' field
def test_copypassword(login_page, copy_text):
    password = "Spotify@123"
    copy = login_page.enter_password("password")
    copy_password = copy_text(copy)
    assert copy_password != password


#  TC_019 - Verify that whether the 'Email or username' and 'Password' field is only accepting spaces.
def test_spaces(login_page, setup):
    login_page.enter_username(" ")
    login_page.enter_password(" ")
    login_page.click_login()
    error_message = login_page.get_error_message()
    expected_error_message = "Incorrect username or password."
    assert error_message == expected_error_message

#  TC_020 - Verify the "Forgot your Password?" link.
def test_resetpassword(login_page, setup):
    login_page.click_forgotpass()
    reset_password = login_page.page_resetpassword()
    expected_page = "Reset your password"
    assert reset_password == expected_page
