from django.test import TestCase
from .models import Videos


class TestVideoModel(TestCase):
    def setUp(self):
        Videos.objects.create(title="This is a title")

    def test_valid_title(self):
        title="This is a title"
        qs = Videos.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Videos.objects.all()
        self.assertEqual(qs.count(), 1)
