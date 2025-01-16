# test_cases/test_login.py
from selenium.common.exceptions import NoAlertPresentException
import pytest
from base.open_browser import BrowserManager
from pages.login_page import LoginPage
from utils.popup_handler import PopupHandler


@pytest.fixture
def setup():
    """Setup fixture to initialize the browser."""
    manager = BrowserManager("chrome")
    driver = manager.get_driver()
    driver.get("https://www.2020exch.com")  # Replace with your login URL
    yield driver
    driver.quit()

def test_valid_login(setup):
    """#Test valid login scenario."""
    login_page = LoginPage(setup)
    login_page.login("Promod423tex", "Promod@36")
    assert "2020EXCH" in setup.title  # Replace with an actual assertion





def test_login_with_popup(setup):
    """Test login and handle popup."""
    login_page = LoginPage(setup)
    login_page.login("valid_username", "valid_password")

    # Handle popup after login
    popup_handler = PopupHandler(setup)
    popup_message = popup_handler.handle_alert()  # or handle_modal_popup(".modal-class")
    assert popup_message == "Expected message", "Popup message does not match!"


