import settings
import teabag.storage as storage
import teabag.cryptographer as cryptographer


def is_message_exists(token):
    try:
        return bool(get_message(token, remove=False))
    except Exception:
        return False


def get_message(token, remove=True):
    id_size = settings.message_id_size
    message_id = token[:id_size].decode('utf-8')
    key = token[id_size:].decode('utf-8')

    ciphertext = storage.load_ciphertext(message_id)
    message = cryptographer.decrypt(key, ciphertext)

    if remove:
        storage.remove_message(message_id)
    return message


def save_message(message):
    if not message:
        raise ValueError('Empty message')

    key, ciphertext = cryptographer.encrypt(message)
    message_id = storage.save_ciphertext(ciphertext)
    token = message_id + key
    return token
