import unittest
import requests
import logging
from html_reporter import HTMLTestRunner

# Configure logging
logging.basicConfig(
    filename="api_test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class TestBasicAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:8000"

    def test_get_users(self):
        """Test the GET /users endpoint."""
        logging.info("Testing GET /users endpoint.")
        response = requests.get(f"{self.BASE_URL}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)
        logging.info(f"GET /users passed. Response: {response.json()}")

    def test_create_user(self):
        """Test the POST /users endpoint."""
        logging.info("Testing POST /users endpoint.")
        new_user = {"id": 3, "name": "Alice", "email": "alice@example.com"}
        response = requests.post(f"{self.BASE_URL}/users", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertDictEqual(response.json(), new_user)
        logging.info(f"POST /users passed. Response: {response.json()}")

    def test_invalid_endpoint(self):
        """Test accessing an invalid endpoint."""
        logging.info("Testing an invalid endpoint.")
        response = requests.get(f"{self.BASE_URL}/invalid")
        self.assertEqual(response.status_code, 404)
        logging.info(f"Invalid endpoint test passed. Response: {response.text}")

if __name__ == "__main__":
    # Generate an HTML report
    with open("api_test_report.html", "w") as report:
        runner = HTMLTestRunner(
            stream=report,
            report_title="API Test Report",
            descriptions="Test results for Basic API.",
        )
        unittest.main(testRunner=runner)
