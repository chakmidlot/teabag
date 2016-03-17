import base64

from Crypto.Cipher import AES
from Crypto import Random


def encrypt(message):
    message_bytes = message.encode('utf-8')
    rest_bytes = b'\x00' * ((16 - len(message_bytes) % 16) % 16)
    message_bytes += rest_bytes

    key = Random.get_random_bytes(24)
    aes = AES.new(key)

    key_base64 = base64.urlsafe_b64encode(key).decode('utf-8')
    ciphertext = aes.encrypt(message_bytes)
    return key_base64, ciphertext


def decrypt(key_base64, ciphertext):
    key = base64.urlsafe_b64decode(key_base64)
    aes = AES.new(key)
    return aes.decrypt(ciphertext).strip(b'\x00').decode('utf-8')
