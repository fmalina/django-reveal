from django.shortcuts import render
from django.http import HttpResponse
from reveal.models import Reveal, get_content_object
from reveal import app_settings
from reveal import cipher


def reveal_info(request, info_attr,
                app_label=None, model=None, object_id=None,
                no_js=None):
    if not request.user.is_authenticated:
        return HttpResponse('login')

    if info_attr not in app_settings.REVEAL_INFO_ATTRS:
        return HttpResponse('not permitted')

    provider = get_content_object(app_label, model, object_id)

    info = getattr(provider, info_attr)
    r = Reveal(enquiring=request.user, info_attr=info_attr)
    r.content_object = provider
    r.save()

    protocol = app_settings.REVEAL_PROTOCOL_MAP[info_attr]

    tpl = 'reveal/reveal_info.html'
    if no_js:
        tpl = 'reveal/reveal.html'

    return render(request, tpl, {
        'info': info,
        'info_attr': info_attr,
        'protocol': protocol
    })


def decrypt_info(request, data):
    if not request.user.is_authenticated:
        return HttpResponse('login')

    info = cipher.decrypt(data)
    return HttpResponse(info)
