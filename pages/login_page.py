# pages/login_page.py
from selenium.webdriver.common.by import By
from base.base_page import BasePage

class LoginPage(BasePage):
    """
    Page Object Model for the Login Page.
    """

    # Locators
    USERNAME_INPUT = (By.NAME, "username")  # Example NAME
    PASSWORD_INPUT = (By.NAME, "password")  # Example NAME
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")    # Example ID
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-msg")  # Example CSS selector

    def __init__(self, driver):
        """
        Constructor for LoginPage.
        :param driver: WebDriver instance.
        """
        super().__init__(driver)

    def enter_username(self, username):
        """Enter the username."""
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        """Enter the password."""
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the login button."""
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        """Get the error message displayed on invalid login."""
        return self.get_text(self.ERROR_MESSAGE)

    def login(self, username, password):
        """
        Perform login with provided credentials.
        :param username: User's username.
        :param password: User's password.
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def handle_post_login_popup(self):
        """Handles any popup that appears after login."""
        # Example for handling different popup types
        try:
            self.handle_js_alert()
        except NoAlertPresentException:
            self.handle_modal_popup()  # Add other popup handlers as needed

