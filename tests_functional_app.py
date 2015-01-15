from selenium import webdriver
import unittest


class IndexPageTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
    def tearDown(self):
        self.browser.quit()
if __name__ == "__main__":
    unittest.main(warnings="ignore")