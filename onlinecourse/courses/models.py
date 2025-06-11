# courses/models.py
import urllib.parse
from django.db import models

class Course(models.Model):
    title       = models.CharField(max_length=200)
    image       = models.ImageField(upload_to='course_images/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='sections'
    )
    title = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = [('course', 'order')]

    def __str__(self):
        return f"{self.course.title} — {self.title}"


class Lesson(models.Model):
    section    = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title      = models.CharField(max_length=200)
    video_url  = models.URLField(
        blank=True,
        null=True,
        help_text="YouTube watch URL (full or just query string: v=…&list=…)"
    )
    order      = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = [('section', 'order')]

    def __str__(self):
        return f"{self.section.title} — {self.title}"

    @property
    def youtube_id(self):
        """
        Extracts the YouTube video ID from a full URL or a query string.
        """
        if not self.video_url:
            return None
        parsed = urllib.parse.urlparse(self.video_url)
        # If they pasted a full URL, use parsed.query; otherwise fallback to parsed.path
        qs = parsed.query or parsed.path.lstrip('/')
        params = urllib.parse.parse_qs(qs)
        return params.get('v', [None])[0]

    @property
    def youtube_playlist(self):
        """
        Extracts the YouTube playlist ID from a full URL or a query string.
        """
        if not self.video_url:
            return None
        parsed = urllib.parse.urlparse(self.video_url)
        qs = parsed.query or parsed.path.lstrip('/')
        params = urllib.parse.parse_qs(qs)
        return params.get('list', [None])[0]
