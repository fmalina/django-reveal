from django.urls import path, include
from reveal.tests.test_views import index

urlpatterns = [
    path('', index),
    path('reveal/', include('reveal.urls')),
]
