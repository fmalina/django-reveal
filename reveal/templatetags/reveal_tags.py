from django.template import Library
from django.utils.safestring import mark_safe
from django.urls import reverse
from reveal import cipher
import re

register = Library()


@register.filter
def cover_phone_number(no):
    result = ''
    for order, digit in enumerate(no):
        if order < 5:
            result = result + digit
        else:
            if order in (5,8,11):
                result = result + ' '
            result = result + '*'
    return result


@register.filter
def cover_email(email):
    """Replaces part of the username with dots
    """
    try:
        [user, domain] = email.split('@')
    except:
        # handle invalid emails... sorta
        user = email
        domain = ''

    if len(user) <= 4:
        user_prefix = user[:1]
    elif len(user) <= 6:
        user_prefix = user[:3]
    else:
        user_prefix = user[:4]

    return '%s&hellip;@%s' % (user_prefix, domain)


@register.filter
def cover_website(website):
    www = website.replace('http://', '').replace('https://', '')
    return '%s&hellip;' % www[:10]


tpl = """
    <a href="#show" class="disabled" id="pull{info_attr}">{covered}</a>
    <a class="btn btn-sm btn-default"
        onclick="reveal('{url}', '{info_attr}', '{protocol}')">
        Reveal
    </a>
"""


@register.filter
def reveal(provider, info_attr):
    url = reverse('reveal', kwargs={
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
    d = dict(url=url, info_attr=info_attr, covered=covered, protocol=protocol)
    button = tpl.format(**d)
    return mark_safe(button)


@register.filter
def mailhide_button(email):
    encrypted = cipher.encrypt(email)
    url = reverse('decrypt', kwargs={'data': encrypted})
    covered = cover_email(email)
    d = dict(url=url, info_attr='email', covered=covered, protocol='mailto:')
    button = tpl.format(**d)
    return """<span class="linkb">
        <i class="glyphicon glyphicon-envelope"></i>
        reveal email: <span>%s</span></span>""" % button


@register.filter
def mailhide_protect(txt):
    """
    testnquiries@mrc-academy.org
    test.banbury@mrc-academy.org
    Columbia.testge@schools.sunderland.gov.uk
    Direct email:gtunnicliffe@cfbt.com
    """
    pattern = re.compile("(?P<user>[A-Za-z-\.]{1,50})@(?P<domain>[a-z-]+\.[a-z-\.]{2,20})")
    for user, domain in pattern.findall(txt):
        em = user+"@"+domain
        txt = txt.replace(em, " "+mailhide_button(em))
    return txt
