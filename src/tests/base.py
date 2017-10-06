import os
import shutil
import unittest

import settings


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        settings.keys_path = '/tmp/teabag_temp_tests'
        if not os.path.exists(settings.keys_path):
            os.makedirs(settings.keys_path)

    def tearDown(self):
        if os.path.exists(settings.keys_path):
            shutil.rmtree(settings.keys_path)
