import os

import settings
import teabag
from tests.base import BaseTestCase


class MessageTest(BaseTestCase):

    def _get_path(self, message_id):
        return os.path.join(settings.keys_path, message_id)

    def test_create_message(self):
        token = teabag.save_message('asdf')
        message_id = token[:settings.message_id_size]
        filename = self._get_path(message_id)
        assert os.path.exists(filename)
