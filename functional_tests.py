from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

options = Options()
options.headless = True

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox(options=options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Begin by checking out the homepage
            self.browser.get('http://localhost:8000')

        # Notice that the page title and header mention a to-do list.
            self.assertIn('To-Do', self.browser.title)
            self.fail('Finish the test!')

        # Invited to enter a to-do item

        # Enters a to-do list item into a text box

        # After entering, the page udpates and the page lists 
        # the item in the list

        # The text box to enter new items is still present. User
        # enters new item

        # Page updates again showing both to-do list items

        # User notices there is text explaining that the user has a 
        # unique URL to access her to-do list items

        # User visits that URL - her to-do list items are still there

        # User exits 


if __name__ == '__main__':
    unittest.main(warnings='ignore')
