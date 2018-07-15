from django.test import TestCase
from django.contrib.auth.models import User
from reveal.models import Reveal


def create_user():
    u = User.objects.first()
    if not u:
        u = User.objects.create_user('Francis', 'francis@example.com', 'test*pw')
        u.save()
    return u


class RevealTestCase(TestCase):
    def setUp(self):
        """Create users Francis and Advice and
        create a record of Francis revealing Advice's email address.
        """
        francis = create_user()
        advice = User.objects.create_user('Advice', 'advice@example.com', 'test*pw')
        advice.save()

        r = Reveal(enquiring=francis, info_attr='email')
        r.content_object = advice
        r.save()

    def test_model(self):
        """This proves Francis looked at Advice's email address on the site.
        """
        r = Reveal.objects.first()
        self.assertEqual(r.pk, 1)
        self.assertEqual(r.enquiring.username, 'Francis')
        self.assertEqual(r.content_object.username, 'Advice')
