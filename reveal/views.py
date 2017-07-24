from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reveal.models import Reveal, get_content_object
from reveal import app_settings
from reveal import cipher


def reveal_info(request, info_attr, app_label=None, model=None, object_id=None):
    if not request.user.is_authenticated():
        return HttpResponse('login')

    if info_attr not in app_settings.REVEAL_INFO_ATTRS:
        return HttpResponse('not premitted')

    provider = get_content_object(app_label, model, object_id)

    info = getattr(provider, info_attr)
    r = Reveal(enquiring=request.user, info_attr=info_attr)
    r.content_object = provider
    r.save()
    return HttpResponse(info)


def decrypt_info(request, data):
    if not request.user.is_authenticated():
        return HttpResponse('login')

    info = cipher.decrypt(data)
    return HttpResponse(info)
