import settings
import storage
import cryptographer


def get_message(token):
    message_id = token[:settings.message_id_size].decode('utf-8')
    key = token[settings.message_id_size:].decode('utf-8')
    ciphertext = storage.load_ciphertext(message_id)
    message = cryptographer.decrypt(key, ciphertext)
    storage.remove_message(message_id)
    return message


def save_message(message):
    key, ciphertext = cryptographer.encrypt(message)
    message_id = storage.save_ciphertext(ciphertext)
    return message_id, key
