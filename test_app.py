import os
import app
import unittest
from tempfile import mkstemp

class FLRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
    def test_index_resolution(self):
        rv = self.app.get('/')
        assertEqual('Translation Memory' in rv.data)
    def tearDown(self):
        os.close(db_fd)
        os.unlink(app.config['DATABASE'])
if __name__ == "__main__":
    unittest.main()