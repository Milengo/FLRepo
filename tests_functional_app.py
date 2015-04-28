from selenium import webdriver
import unittest


class FLRepoTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_basetemplate(self):
        # application should be running
        self.browser.get('http://localhost:5000')
        # application title should display the name
        # "Translation Unit Repository
        self.assertIn('Translation Units Repository', self.browser.title)
        # 4 menu options should be visible in navigation bar
        self.assertIn('Home', self.browser.find_element_by_id('home').text)
        self.assertIn(
            'Upload TM',
            self.browser.find_element_by_id('upload').text)
        self.assertIn(
            'List of Memoq TMs',
            self.browser.find_element_by_id('tm_list').text)
        self.assertIn('About', self.browser.find_element_by_id('about').text)
        # and a div container
        self.assertTrue(self.browser.find_element_by_class_name('container'))

    def test_uploadTM(self):
        # application should be running
        self.browser.get('http://localhost:5000')
        # user clicks on the upload TM link
        button = self.browser.find_element_by_id('upload')
        button.click()
        # it redirects to the "/upload" page with the header : Upload TM
        self.assertIn(
            "Upload TM",
            self.browser.find_element_by_tag_name("h1").text)
        # there should be a button named "choose file"
        self.assertTrue(self.browser.find_element_by_id('file'))
        # and the list of Translations memories uploaded to the server
        self.assertTrue(self.browser.find_element_by_id('tms'))
        # clicking on "choose file" should open "select file" dialog
        upload_file_btn = self.browser.find_element_by_id('file')
        upload_file_btn.click()
        self.browser.switchTo().activeElement().sendKeys(
            'c:\Sites\flrepo\FLRepo\media\CON-CC_Working_en2es-mx_201412450_SW.tmx')

        # after file is uploaded, the list of TMs is refreshed
        # to have one additional TM added
        # for each TM, a full TM name should be visible
        # and a button named "Read data"
        # at the bottom we have a link that goes back to index page
        self.fail("Finish the test")
if __name__ == "__main__":
    unittest.main(warnings="ignore")
