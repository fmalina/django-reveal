from django.conf.urls import url
from reveal.views import reveal_info, decrypt_info

urlpatterns = [
    url(r'^(?P<app_label>[a-z]+)-(?P<model>[a-z]+)/(?P<object_id>[0-9]+)/(?P<info_attr>[a-z0-9]+)$',
        reveal_info, name='reveal'),
    url(r'^decrypt/(?P<data>(.*))$',
        decrypt_info, name='decrypt'),
]
