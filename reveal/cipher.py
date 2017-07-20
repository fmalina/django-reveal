from django.conf import settings
from Crypto.Cipher import Blowfish
import base64


def decrypt(code):
    """Decrypt code encrypted by cipher.encrypt
    """
    secret_key = settings.SECRET_KEY
    encryption_object = Blowfish.new(secret_key)
    # strip padding from decrypted credit card number
    return encryption_object.decrypt(base64.b64decode(code)).decode().rstrip('X')


def encrypt(data):
    """Encrypt data.
    """
    secret_key = settings.SECRET_KEY
    encryption_object = Blowfish.new(secret_key)
    # block cipher length must be a multiple of 8
    padding = ''
    if (len(data) % 8) != 0:
        padding = 'X' * (8 - (len(data) % 8))
    return base64.b64encode(encryption_object.encrypt(data + padding))
