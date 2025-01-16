# base/open_browser.py
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class BrowserManager:
    """
    A class to manage WebDriver initialization for supported browsers.
    """

    def __init__(self, browser_name):
        self.browser_name = browser_name.lower()
        self.driver = None
        self.initialize_driver()

    def initialize_driver(self):
        """Initialize the WebDriver based on the browser name."""
        logging.info(f"Initializing driver for browser: {self.browser_name}")
        if self.browser_name == 'chrome':
            options = ChromeOptions()
            self.driver = webdriver.Chrome(service=ChromeService(), options=options)
        elif self.browser_name == 'safari':
            self.driver = webdriver.Safari(service=SafariService())
        elif self.browser_name == 'edge':
            options = EdgeOptions()
            self.driver = webdriver.Edge(service=EdgeService(), options=options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")
        logging.info(f"Driver initialized successfully for {self.browser_name}")

    def get_driver(self):
        """Return the WebDriver instance."""
        return self.driver

    def close_browser(self):
        """Close the browser."""
        try:
            if self.driver:
                logging.info(f"Closing browser: {self.browser_name}")
                self.driver.quit()
        except Exception as e:
            logging.error(f"Error closing browser: {self.browser_name} - {e}")
            raise
