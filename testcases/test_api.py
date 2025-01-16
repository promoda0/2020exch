import unittest
import requests

class TestAPI(unittest.TestCase):
    BASE_URL = "http://127.0.0.1:5000"

    def test_get_users(self):
        response = requests.get(f"{self.BASE_URL}/users")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_user(self):
        new_user = {"id": 3, "name": "Alice", "email": "alice@example.com"}
        response = requests.post(f"{self.BASE_URL}/users", json=new_user)
        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(new_user, response.json())

if __name__ == "__main__":
    unittest.main()
