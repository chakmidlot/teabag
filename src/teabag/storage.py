import os
import base64

from Crypto import Random

import settings
import teabag.shredder as shredder


def save_ciphertext(ciphertext):
    random_bytes = Random.get_random_bytes(settings.message_id_size * 3 // 4)
    message_id = base64.urlsafe_b64encode(random_bytes).decode('utf-8')
    with open(_get_path(message_id), 'wb') as f:
        f.write(ciphertext)
    return message_id


def load_ciphertext(message_id):
    path = _get_path(message_id)
    with open(path, 'rb') as f:
        ciphertext = f.read()
    return ciphertext


def remove_message(message_id):
    shredder.remove_file(_get_path(message_id))


def is_exists(message_id):
    return os.path.exists(_get_path(message_id))


def _get_path(message_id):
    return os.path.join(settings.keys_path, message_id)
