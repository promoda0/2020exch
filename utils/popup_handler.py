from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PopupHandler:
    def __init__(self, driver):
        self.driver = driver

    def handle_modal_popup(self, popup_locator):
        """Handles modal dialogs."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, popup_locator))  # Update locator
            )
            popup = self.driver.find_element(By.CSS_SELECTOR, popup_locator)
            popup_text = popup.text
            print(f"Popup message: {popup_text}")
            close_button = self.driver.find_element(By.CSS_SELECTOR, "button.close")  # Update if needed
            close_button.click()
            return popup_text
        except Exception as e:
            print(f"Error handling modal popup: {e}")
            return None
