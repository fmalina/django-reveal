from django.conf import settings
from cryptography.fernet import Fernet


def decrypt(code):
    """Decrypt code encrypted by cipher.encrypt"""
    f = Fernet(settings.SECRET_KEY)
    return f.decrypt(code).decode('ascii')


def encrypt(data):
    """Encrypt data."""
    f = Fernet(settings.SECRET_KEY)
    return f.encrypt(data)
