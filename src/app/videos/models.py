from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    videos_id = models.CharField(max_length=255)


class VideoProxy(Videos):
    class Meta:
        proxy = True
        verbose_name = "Published Video"
        verbose_name_plural = "Published Videos"
