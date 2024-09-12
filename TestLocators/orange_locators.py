"""
orange_locators.py

Program : File containing the Locators for OrangeHRM
"""


class OrangeHRM_Locators:

   username = "username"
   password = "password"
   submit_button = "//button[@type='submit']"
   admin_button = "//span[text()='Admin']"
   forgot_password_link_button = "//p[text()='Forgot your password? ']"
   reset_password_button = "//div[@class='orangehrm-forgot-password-button-container']//button[2]"
   reset_password_text = "//div[@class='orangehrm-card-container']//h6"
   header_options = "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li"
   menu_options = "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span"


