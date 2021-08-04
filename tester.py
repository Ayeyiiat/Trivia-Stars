import unittest, sys

sys.path.append('../Trivia_Stars') # imports python file from parent directory
from app import app #imports flask app object

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_main_page(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_main_page(self):
        response = self.app.get('/leaderboard', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
      
    '''def test_main_page(self):
        response = self.app.get('/quiz<room>', follow_redirects=True)
        self.assertEqual(response.status_code, 200)'''

    '''def test_main_page(self):
        response = self.app.get('/solo/game', follow_redirects=True)
        self.assertEqual(response.status_code, 200)'''
        
    
if __name__ == "__main__":
    unittest.main()
