from django import test
from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from db.models import PublishStateOptions
from .models import Video


class TestVideoModel(TestCase):
    def setUp(self):
        self.obj_1 = Video.objects.create(
            title="This is a title", videos_id="test")
        self.obj_2 = Video.objects.create(
            title="This is a title", videos_id="test1",
            state=PublishStateOptions.PUBLISHED)

    def test_valid_title(self):
        title = "This is a title"
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_slug_field(self):
        title = self.obj_1.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_1.slug)

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Video.objects.filter(state=PublishStateOptions.PUBLISHED)
        now = timezone.now()
        published_qs = Video.objects.filter(
            state=PublishStateOptions.PUBLISHED,
            publish_timestamp__lte=now
        )
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs_1 = Video.objects.all().published()
        published_qs_2 = Video.objects.published()
        self.assertTrue(published_qs_1.exists())
        self.assertEqual(published_qs_1.count(), published_qs_2.count())
