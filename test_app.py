import os
import app
import unittest
import tempfile

class FLRepoTestCase(unittest.TestCase):
    def setUp(self):
        self.db_fd, app.config['DATABASE'] = tempfile.mkstemp()
        app.config['TESTING'] = True
        self.app = app.test_client()
    def tearDown(self):
        os.close(db_fd)
        os.unlink(app.config['DATABASE'])
if __name__ == "__main__":
    unittest.main()