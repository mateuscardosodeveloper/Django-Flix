from django import test
from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

from djangoflix.db.models import PublishStateOptions
from videos.models import Video
from .models import Playlist


class TestPlaylistModel(TestCase):
    def create_videos(self):
        video_1 = Video.objects.create(
            title="This is a title", videos_id="test1")
        video_2 = Video.objects.create(
            title="This is a title", videos_id="test2")
        video_3 = Video.objects.create(
            title="This is a title", videos_id="test3")
        self.video_1 = video_1
        self.video_2 = video_2
        self.video_3 = video_3
        

    def setUp(self):
        self.create_videos()
        self.obj_1 = Playlist.objects.create(
            title="This is a title", video=self.video_1)
        obj_2 = Playlist.objects.create(
            title="This is a title", video=self.video_1,    
            state=PublishStateOptions.PUBLISHED)
        video_qs = Video.objects.all()
        obj_2.videos.set(video_qs)
        obj_2.save()
        self.obj_2 = obj_2

    
    def test_playlist_video(self):
        self.assertEqual(self.obj_1.video, self.video_1)

    def test_playlist_video_items(self):
        count = self.obj_2.videos.all().count()
        self.assertEqual(count, 3)

    def test_video_playlist_ids_propery(self):
        ids = self.obj_1.video.get_playlist_ids()
        actual_ids = list(Playlist.objects.filter(video=self.video_1).values_list(
            'id',  flat=True
        ))
        self.assertEqual(ids, actual_ids)

    def test_video_playlist(self):
        qs = self.video_1.playlist_featured.all()
        self.assertEqual(qs.count(), 2)

    def test_valid_title(self):
        title = "This is a title"
        qs = Playlist.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_slug_field(self):
        title = self.obj_1.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.obj_1.slug)

    def test_created_count(self):
        qs = Playlist.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        qs = Playlist.objects.filter(state=PublishStateOptions.PUBLISHED)
        now = timezone.now()
        published_qs = Playlist.objects.filter(
            state=PublishStateOptions.PUBLISHED,
            publish_timestamp__lte=now
        )
        self.assertTrue(published_qs.exists())

    def test_publish_manager(self):
        published_qs_1 = Playlist.objects.all().published()
        published_qs_2 = Playlist.objects.published()
        self.assertTrue(published_qs_1.exists())
        self.assertEqual(published_qs_1.count(), published_qs_2.count())
