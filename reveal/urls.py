from django.urls import path
from reveal import views

reveal_url = '<slug:app_label>-<slug:model>/<int:object_id>/<slug:info_attr>'
urlpatterns = [
    path(reveal_url, views.reveal_info, name='reveal'),
    path('link/' + reveal_url, views.reveal_info, {'no_js': True}, name='reveal_nojs'),
    path('decrypt/<path:data>', views.decrypt_info, name='decrypt'),
]
