from django.conf.urls import url, include
from reveal.tests.test_views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^reveal/', include('reveal.urls')),
]
