# base/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class BasePage:
    """
    Base class for all page objects.
    """

    def __init__(self, driver):
        """
        Constructor for BasePage.
        :param driver: WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)  # Explicit wait with a timeout of 10 seconds

    def click_element(self, locator):
        """Click an element."""
        logging.info(f"Clicking element: {locator}")
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Enter text into an input field."""
        logging.info(f"Entering text '{text}' into element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from an element."""
        logging.info(f"Getting text from element: {locator}")
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
