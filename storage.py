import os
import base64

from Crypto import Random

import settings
import shredder


class FileNotFound(Exception):
    pass


def save_ciphertext(ciphertext):
    random_bytes = Random.get_random_bytes(settings.message_id_size * 3 // 4)
    message_id = base64.urlsafe_b64encode(random_bytes).decode('utf-8')

    file_path = os.path.join(settings.keys_path, message_id)
    open(file_path, 'wb').write(ciphertext)

    return message_id


def load_ciphertext(message_id):
    path = os.path.join(settings.keys_path, message_id)

    try:
        ciphertext = open(path, 'rb').read()
    except FileNotFoundError:
        raise FileNotFound

    shredder.remove_file(path)
    return ciphertext
