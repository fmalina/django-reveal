Django app to track and control access to protected details
===========================================================

.. image:: https://travis-ci.org/fmalina/django-reveal.svg?branch=master
    :target: https://travis-ci.org/fmalina/django-reveal

A reusable Django app for tracking user access to protected details.

- protect access to email addresses, hide them from harvesters
- protect access to phone numbers and track which users accessed the number
- login only hyperlinks for registered human users only with tracking

Installation (into a Django project)
------------------------------------

To get the latest version from GitHub

::

    pip3 install -e git+git://github.com/fmalina/django-reveal.git#egg=reveal

Add ``reveal`` to your ``INSTALLED_APPS``

::

    INSTALLED_APPS = (
        ...,
        'reveal',
    )

Configure your settings to suit, see reveal/app_settings.py.

Add the ``reveal`` URLs to your ``urls.py``

::

    urlpatterns = [
        ...
        url(r'^reveal/', include('reveal.urls')),
    ]

Create your tables

::

    ./manage.py migrate reveal


Usage
-----
Simple integration works out of the box.

To cover/reveal a phone number for a person, just use a filter on the person:

::
	{% include 'reveal/reveal.js' %}

	{% if user.is_authenticated %}
		Phone: {{ person|reveal:'phone' }}
	{% else %}
		Phone: {{ person.phone|cover_phone_number }}
	{% endif %}


Contribute
----------
File issues. Fork and send pull requests. Tell developers integrating payments.

Thank you.
