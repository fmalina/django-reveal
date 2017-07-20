from django.test import TestCase
from django.contrib.auth.models import User
from reveal.models import Reveal


def create_user():
    u = User.objects.first()
    if not u:
        u = User.objects.create_user('Frank', 'hooray@example.com', 'testpw')
        u.save()
    return u


class RevealTestCase(TestCase):
    def setUp(self):
        u = create_user()
        c = Reveal.objects.create(user=u)
        c.save()

    def test_model(self):
        f = Reveal.objects.first()
        self.assertEqual(f.pk, 1)
        self.assertEqual(f.alt, 'Frank')
        self.assertTrue(f.path().endswith('upload/static/media/0/1/1.jpg'))
