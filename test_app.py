import os
import mainapp
import unittest
from unittest.mock import patch
from tempfile import mkstemp



class FLRepoTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, mainapp.app.config['DATABASE'] = mkstemp()
        mainapp.app.config['TESTING'] = True
        self.app = mainapp.app.test_client()

    def test_index_resolution(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(mainapp.app.config['DATABASE'])

    @patch('mainapp.views.MemoqTMClient')
    def test_download_tm_route_redirects_to_same_url(self, mock):
        mock.export_tmx("some_global", "filename").return_value = None

        rv = self.app.get('/tm_download/{guid}/{name}'.format(
            guid='some_global', name='filename'))
        self.assertEqual(rv.status, '200')



if __name__ == "__main__":
    unittest.main()
