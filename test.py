import unittest
import app as app

class FlaskAppTests(unittest.TestCase):
    
    def setUp(self):
        self.app = app.app.test_client()
    
    def test_app(self):
        r = self.app.get('/')
        self.assertEqual(r._status_code, 200)
        
    def test_sumOfAP(self):
        self.assertEqual(app.sumOfAP(1, 1, 3), 6)

if __name__ == '__main__':
    unittest.main()