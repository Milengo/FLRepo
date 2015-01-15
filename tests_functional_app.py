from selenium import webdriver
import unittest


class IndexPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()
    def test_homepage(self):
        #application should be running
        self.browser.get('http://localhost:5000')
        #application title should display the name "Translation Unit Repository
        self.assertIn('Translation Units Repository', self.browser.title)
        #4 menu options should be visible in navigation bar
        self.assertIn('Home', self.browser.find_element_by_id('home').text)
        self.assertIn('Upload TM', self.browser.find_element_by_id('upload').text)
        self.assertIn('List of Memoq TMs', self.browser.find_element_by_id('tm_list').text)
        self.assertIn('About', self.browser.find_element_by_id('about').text)
        #and a div container
        self.assertTrue(self.browser.find_element_by_class_name('container'))
        
if __name__ == "__main__":
    unittest.main(warnings="ignore")