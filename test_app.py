import os
import mainapp
import unittest
from flask import Flask
from flask.ext.testing import TestCase
from unittest.mock import patch

from tempfile import mkstemp


class FLRepoTestCase(TestCase):

    def create_app(self):

        app = Flask(__name__)
        app.config['TESTING'] = True
        return app

    def setUp(self):
        self.db_fd, mainapp.app.config['DATABASE'] = mkstemp()
        mainapp.app.config['TESTING'] = True
        self.app = mainapp.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(mainapp.app.config['DATABASE'])

    def test_index_resolution(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    @patch('mainapp.views.MemoqTMClient', autospec=True)
    def test_download_tm_route_executes_call_to_api(self, mock):
        mock.export_tmx("some_global", "filename").return_value = True

        self.app.get('/tm_download/{guid}/{name}'.format(
            guid='some_global', name='filename'))
        mock.export_tmx.assert_called_once_with('some_global', 'filename')

    @patch('mainapp.views.MemoqTMClient', autospec=True)
    def test_download_tm_route_returns_200(self, mock):
        temp_tm, filename = mkstemp(dir=mainapp.app.config['UPLOAD_FOLDER'])
        mock.export_tmx("some_global", filename).return_value = True
        tm_name = '.'.join([filename.split(r'\\')[-1], 'tmx'])
        print(tm_name)
        rv = self.app.get('/tm_download/{guid}/{name}'.format(
            guid='some_global', name=tm_name))
        self.assert_template_used('tm_list.html')
        self.assertEqual(rv.status, "200 OK")
        os.close(temp_tm)

if __name__ == "__main__":
    unittest.main()
