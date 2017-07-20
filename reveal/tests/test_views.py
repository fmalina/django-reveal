from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
from reveal.tests.test_models import create_user


def index(request):
    # create dummy account and login the current user
    u = create_user()
    u = authenticate(username=u.username, password='testpw',
        email='fmalina@gmail.com')
    login(request, u)

    return render(request, 'index.html', {
        'user': u
    })
