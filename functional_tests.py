from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import time

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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # Invited to enter a to-do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # Enters a to-do list item into a text box
        inputbox.send_keys('Buy peacock feathers')

        # After entering, the page udpates and the page lists 
        # the item in the list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )


        # The text box to enter new items is still present. User
        # enters new item
        self.fail('finish the test')

        # Page updates again showing both to-do list items

        # User notices there is text explaining that the user has a 
        # unique URL to access her to-do list items

        # User visits that URL - her to-do list items are still there

        # User exits 


if __name__ == '__main__':
    unittest.main(warnings='ignore')
