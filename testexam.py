import unittest
import exam as tested_app
import json

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        self.app = tested_app.app.test_client()

if __name__ == '__main__':
    unittest.main()