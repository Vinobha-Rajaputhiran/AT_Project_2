"""
test_orange.py

Program : POM main executing file
"""

from TestLocators.orange_locators import OrangeHRM_Locators
from TestData.orange_data import OrangeHRM_Data
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchWindowException
import pytest

class Test_OrangeHRM:

    @pytest.fixture
    # Booting function for running all the Python tests
    def booting_function(self):
        firefox_options = Options()
        firefox_options.add_argument('--incognito')
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        yield
        self.driver.close()

    # Method for user login
    def user_login(self):
        try:

            self.driver.get(OrangeHRM_Data.url)

            username_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().username)))
            username_box.send_keys(OrangeHRM_Data.admin_username)

            password_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().password)))
            password_box.send_keys(OrangeHRM_Data.positive_password)

            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators().submit_button)))
            submit_button.click()

            if OrangeHRM_Data().dashboard_url_login == self.driver.current_url:

                admin_button = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.admin_button)))
                admin_button.click()

                if OrangeHRM_Data().dashboard_url_admin_page == self.driver.current_url:

                    return True

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, WebDriverException] as error:
            print('Error:', error)

    # Method to check the header menu options
    def check_header_options(self):

        header_options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, OrangeHRM_Locators.header_options)))

        for options in header_options:

            if options.text not in OrangeHRM_Data.header_options:

                print(f"Failure: {options.text} is not visible in Main Menu")

                raise NoSuchElementException

        return True

    # Method to check the main menu options
    def check_main_menu_options(self):

        main_menu_options = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, OrangeHRM_Locators.menu_options)))

        for options in main_menu_options:

            if options.text not in OrangeHRM_Data.main_menu_options:

                print(f"Failure: {options.text} is not visible in Header Menu")

                raise NoSuchElementException

        return True

    # Test Case for forgot password link validation
    def test_forgot_password_link(self,booting_function):
        try:

            self.driver.get(OrangeHRM_Data.url)

            forgot_password_link = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators().forgot_password_link_button)))
            forgot_password_link.click()

            if OrangeHRM_Data().dashboard_url_forgot_password == self.driver.current_url:

                username_box = self.wait.until(EC.presence_of_element_located((By.NAME, OrangeHRM_Locators().username)))
                username_box.send_keys(OrangeHRM_Data.forgot_password_username)

                reset_password = self.wait.until(EC.element_to_be_clickable((By.XPATH, OrangeHRM_Locators.reset_password_button)))
                reset_password.click()

                message = self.wait.until(EC.presence_of_element_located((By.XPATH, OrangeHRM_Locators.reset_password_text))).text
                assert message == OrangeHRM_Data.password_reset_message

                print("SUCCESS : Reset Password Message Validated")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)


    # Test Case to validate header title
    def test_header_title(self, booting_function):
        try:

            if self.user_login():

                assert self.driver.title == OrangeHRM_Data.title and self.check_header_options() == True

                print("SUCCESS: Webpage Title and Options Validated")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)


    # Test Case to edit existing employee information
    def test_main_menu(self, booting_function):
        try:

            if self.user_login():

                assert self.check_main_menu_options() == True

                print("SUCCESS : Main Menu Options Validated")

        except [NoSuchElementException, TimeoutException, ElementClickInterceptedException, ElementNotVisibleException, NoSuchWindowException, WebDriverException] as error:
            print('Error:', error)




