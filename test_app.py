import os
import mainapp
import unittest
from tempfile import mkstemp


class FLRepoTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, mainapp.app.config['DATABASE'] = mkstemp()
        mainapp.app.config['TESTING'] = True
        self.app = mainapp.app.test_client()

    def test_index_resolution(self):
        rv = self.app.get('/')
        print(rv.data)

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(mainapp.app.config['DATABASE'])

if __name__ == "__main__":
    unittest.main()
