from django.template import Library
from django.utils.safestring import mark_safe
from django.urls import reverse
from reveal import cipher
import re
import uuid

register = Library()


EMAIL_RE = r'(?i)\b[a-z0-9._%-]+\s*(?:@| at |\[at\])\s*[a-z\d.-]+\s*(?:\.|dot|\[dot\])\s*[a-z]{2,4}\b'
PHONE_RE = r'[0-9OIl\ \-\+\/\.\(\)]{11,}'
URL_RE = r'[\w.|:|/]+\.(com|net|org|co\.uk|ac\.uk)[\w.|\.|/|-]{0,}'


@register.filter
def hide_contact(s):
    s = re.sub(EMAIL_RE, ' (email hidden) ', s)
    s = re.sub(PHONE_RE, ' (phone hidden) ', s)
    if settings.DOMAIN not in s:
        s = re.sub(URL_RE, ' (URL hidden) ', s)
    return s


def short_random_hash():
    return str(uuid.uuid4())[:8]


@register.filter
def cover_phone_number(no):
    """
    >>> cover_phone_number('01234 567 890')
    '01234 *** *** **'
    """
    result = ''
    for order, digit in enumerate(no):
        if order < 5:
            result = result + digit
        else:
            if order in (5, 8, 11):
                result = result + ' '
            result = result + '*'
    return result


@register.filter
def cover_email(email):
    """Replaces part of the username with dots

    >>> cover_email('hello@example.com')
    'hel&hellip;@example.com'
    """
    try:
        [user, domain] = email.split('@')
    except ValueError:
        # handle invalid emails... sorta
        user = email
        domain = ''

    if len(user) <= 4:
        user_prefix = user[:1]
    elif len(user) <= 6:
        user_prefix = user[:3]
    else:
        user_prefix = user[:4]

    return f'{user_prefix}&hellip;@{domain}'


@register.filter
def cover_website(website):
    """
    >>> cover_website('https://unilexicon.com/vocabularies/')
    'unilexicon&hellip;'
    """
    www = website.replace('http://', '').replace('https://', '')
    return f'{www[:10]}&hellip;'


tpl = """
    <a href="#show" class="disabled" id="{identifier}">{covered}</a>
    <button onclick="reveal('{url}', '{info_attr}', '{protocol}', '{identifier}')"
            class="btn btn-sm btn-reveal">reveal</button>
"""

tpl_nojs = """
    <a href="#show" class="disabled">{covered}</a>
    <a class="btn btn-reveal" href="{url}">reveal</a>
"""


def reveal_button(provider, info_attr, template, url_patt):
    url = reverse(url_patt, kwargs={
        'app_label': provider._meta.app_label,
        'model': provider.__class__.__name__.lower(),
        'object_id': provider.pk,
        'info_attr': info_attr
    })

    info = getattr(provider, info_attr)

    cover_func = {
        'phone': cover_phone_number,
        'phone2': cover_phone_number,
        'email': cover_email,
        'website': cover_website
    }[info_attr]

    protocol = {
        'phone': 'tel:',
        'phone2': 'tel:',
        'email': 'mailto:',
        'website': '',
    }[info_attr]

    covered = cover_func(info)

    d = dict(url=url, info_attr=info_attr,
             covered=covered, protocol=protocol,
             identifier=short_random_hash())
    button = template.format(**d)
    return mark_safe(button)


@register.filter
def reveal(provider, info_attr):
    return reveal_button(provider, info_attr, tpl, 'reveal')


@register.filter
def reveal_nojs(provider, info_attr):
    return reveal_button(provider, info_attr, tpl_nojs, 'reveal_nojs')


@register.filter
def mailhide_button(email):
    """
    Encrypt an email address
    display instead a reveal button that allow logged-in
    system users to decrypt it.
    """
    encrypted = cipher.encrypt(email).decode()
    url = reverse('decrypt', kwargs={'data': encrypted})
    covered = cover_email(email)
    identifier = short_random_hash()
    d = dict(url=url, info_attr='email', covered=covered,
             protocol='mailto:', identifier=identifier)
    button = tpl.format(**d)
    return f"""<abbr id="{identifier}" class="reveal-email"
                    title="reveal email">{button}</abbr>"""


@register.filter
def mailhide_protect(txt):
    """
    Encrypt all email addresses found in text showing mailhide buttons insted.

    testnquiries@mrc-academy.org
    test.banbury@mrc-academy.org
    Columbia.testge@schools.sunderland.gov.uk
    Direct email:gtunnicliffe@cfbt.com
    """
    pattern = re.compile("(?P<user>[A-Za-z-\.]{1,50})@(?P<domain>[A-Za-z-]+\.[a-z-\.]{2,20})")
    for user, domain in pattern.findall(txt):
        em = user+"@"+domain
        txt = txt.replace(em, " "+mailhide_button(em))
    return txt
