from django.conf import settings


REVEAL_INFO_PROVIDER = getattr(settings, 'REVEAL_INFO_PROVIDER',
    settings.AUTH_USER_MODEL)
