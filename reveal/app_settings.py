from django.conf import settings

# permitted attributes to reveal
REVEAL_INFO_ATTRS = getattr(settings, 'REVEAL_INFO_ATTRS',
    ['phone', 'phone2', 'website', 'email'])

REVEAL_PROTOCOL_MAP = getattr(settings, 'REVEAL_PROTOCOL_MAP', {
    'phone': 'tel:',
    'phone2': 'tel:',
    'email': 'mailto:',
    'website': '',
})
