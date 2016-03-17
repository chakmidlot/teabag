import settings
import storage
import cryptographer


def get_message(token):
    id_size = settings.message_id_size
    message_id = token[:id_size].decode('utf-8')
    key = token[id_size:].decode('utf-8')

    ciphertext = storage.load_ciphertext(message_id)
    message = cryptographer.decrypt(key, ciphertext)

    storage.remove_message(message_id)
    return message


def save_message(message):
    if not message:
        raise ValueError('Empty message')
    key, ciphertext = cryptographer.encrypt(message)
    message_id = storage.save_ciphertext(ciphertext)
    return message_id, key
