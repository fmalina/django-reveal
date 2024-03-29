Protect access to sensitive personal information
================================================

.. image:: https://travis-ci.org/fmalina/django-reveal.svg?branch=main
    :target: https://travis-ci.org/fmalina/django-reveal

A reusable Django app for protecting personal details.

Out of the box features:

✉️ 🙋 protect access to email addresses, hide them from harvesters

🚫 🤖 use as an alternative to discontinued ReCaptcha Mailhide

Hide contact details in user entered text and messages for containment

🔒 📞 protect access to phone numbers and track which users accessed the number

🔗 👤 show certain content pieces only to registered users with access log


Imagine you run an online classifieds website or business directory where
users want to share personal details such as email addresses
and phone numbers to be contacted by other users.

Say you want to implement a cap, so that a regular user can only reveal
so many personal details per hour or per day to prevent spamming.

Or you may want to know who contacted who to ask them later how it went.

Or you may want to protect email addresses in text on your site so that
spambots can not harvest them.

This app along with auth and your own throttling caps or business model
helps you with user friendly protection of data and logging reveals.

Usage
-----
Simple integration works out of the box.

To cover/reveal a phone number for a person, just use a filter on the person:

::

	<script>{% include 'reveal/reveal.js' %}</script>

	<p>Phone: {{ organisation|reveal:'phone' }}
	<p>Website: {{ organisation|reveal:'website' }}

or

::

    {% if not user.is_authenticated %}
            Phone: {{ person.phone|cover_phone_number }}<br>
            Email: {{ person.email|cover_email }}
    {% endif %}

or

::

  <div class="official_report">
    {{ report.text|mailhide_protect }}
  </div>

Hide contact details in messages and posts (email addresses, phone numbers, URLs).

::

  {% load reveal_tags %}

  <div class="message">
    {{ message.body|hide_contact }}
  </div>

Or just discard them before saving a message.

::

  from reveal.templatetags.reveal_tags import hide_contact

  message.body = hide_contact(message.body)
  message.save()

Available template filters used for display of placeholder information:

- ``|cover_email }}`` (``hello@example.com -> hel...@example.com``)
- ``|cover_phone_number }}`` (``01234 567 890 -> 01234 *** *** **``)
- ``|cover_website }}`` (``https://unilexicon.com/vocabularies/ -> unilexicon...``)

Template tags for displaying reveal buttons that show
protected data when clicked:

- ``reveal`` this will show a partially covered phone number with a reveal button.
There is a JS version using vanilla XHR, asking a user to login or
just making a XHR call and revealing details in place.
- ``reveal_nojs`` no JS version for AMP that reveals protected details
to logged in users in a new window.

For protection of email addresses in text, similar to old ReCaptcha mailhide.

- ``mailhide_button(email)`` encrypt an email address and display instead
  a reveal button that allows logged-in system users to see decrypted one
- ``mailhide_protect(txt)`` encrypt all email addresses found
  in text showing mailhide buttons instead.


Installation (into a Django project)
------------------------------------

To get the latest version from GitHub

::

    pip3 install -e git+git://github.com/fmalina/django-reveal.git#egg=reveal

Add ``reveal`` to your ``INSTALLED_APPS``

.. code:: python

    INSTALLED_APPS = (
        ...,
        'reveal',
    )

Configure your settings to suit, see reveal/app_settings.py.

Add the ``reveal`` URLs to your ``urls.py``

.. code:: python

    urlpatterns = [
        ...
        path('reveal/', include('reveal.urls')),
    ]

Create your tables

::

    ./manage.py migrate reveal
