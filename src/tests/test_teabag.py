import os

import settings
import teabag
from tests.base import BaseTestCase


class MessageTest(BaseTestCase):

    def _get_path(self, message_id):
        return os.path.join(settings.keys_path, message_id)

    def _to_bytes(self, string):
        return bytes(string, 'utf-8')

    def test_create_message(self):
        token = teabag.save_message('asdf')
        message_id = token[:settings.message_id_size]
        filename = self._get_path(message_id)
        assert os.path.exists(filename)

    def test_get_message(self):
        token = teabag.save_message('asdf')
        message = teabag.get_message(self._to_bytes(token))
        assert message == 'asdf'

    def test_message_removed(self):
        token = teabag.save_message('asdf')
        message_id = token[:settings.message_id_size]
        filename = self._get_path(message_id)
        teabag.get_message(self._to_bytes(token))
        assert not os.path.exists(filename)

    def test_message_exists(self):
        token = teabag.save_message('asdf')
        exists = teabag.is_message_exists(self._to_bytes(token))
        assert exists

    def test_message_not_exists(self):
        token = 'koDg1NBlsXTiGstJYvvNCl7euXki8RjamPmlZusT'
        exists = teabag.is_message_exists(self._to_bytes(token))
        assert not exists
