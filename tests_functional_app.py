from selenium import webdriver
import unittest


class IndexPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
    def tearDown(self):
        self.browser.quit()
    def test_title(self):
        self.browser.get('http://localhost:5000')
        self.assertIn('Translation', self.browser.title)
        self.fail('Finish the test')
if __name__ == "__main__":
    unittest.main(warnings="ignore")