import base64
import os

from Crypto import Random

import settings


def save_ciphertext(ciphertext):
    random_bytes = Random.get_random_bytes(settings.message_id_size * 3 // 4)
    message_id = base64.urlsafe_b64encode(random_bytes).decode('utf-8')

    file_path = os.path.join(settings.keys_path, message_id)
    open(file_path, 'wb').write(ciphertext)

    return message_id


def load_ciphertext(message_id):
    path = os.path.join(settings.keys_path, message_id)
    ciphertext = open(path, 'rb').read()
    os.remove(path)

    return ciphertext
