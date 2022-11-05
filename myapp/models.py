from django.db import models

class Talk(models.Model):

    # https://aeracode.org/2022/11/03/static-dynamic-in-memory-sqlite/
    __yamdl__ = True  # See what this means at the end of the blog post

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    length = models.IntegerField(blank=True, null=True)
    keynote = models.BooleanField(default=False)

    when = models.DateField()
    conference = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=2, blank=True, null=True)

    slides_url = models.URLField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)