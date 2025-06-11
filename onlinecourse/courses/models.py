# courses/models.py
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


from django.db import models

class Lesson(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title = models.CharField(max_length=200)

    # Either video or PDF path stored in Supabase
    file_path = models.CharField(
        max_length=500,
        blank=True,
        help_text="Supabase path, e.g. 'folder/filename.mp4' or 'folder/filename.pdf'"
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = [('section', 'order')]

    def __str__(self):
        return f"{self.section.title} — {self.title}"

    @property
    def is_pdf(self):
        return self.file_path.lower().endswith('.pdf')

    @property
    def is_video(self):
        return self.file_path.lower().endswith(('.mp4', '.mov', '.avi'))
