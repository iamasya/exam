import unittest
import exam as app
import json

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.app.test_client()
    
    # def test_home(self):
    #     self.assertTrue(app.home)
    def test_app(self):
        r = self.app.get('/')
        self.assertEqual(r._status_code, 200)
        
    def test_sumOfAP(self):
        self.assertEqual(app.sumOfAP(2, 2, 5), 30)

if __name__ == '__main__':
    unittest.main()