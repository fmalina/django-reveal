from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from reveal.tests.test_views import index

urlpatterns = [
    url(r'^$', index),
    url(r'^reveal/', include('reveal.urls')),
]
