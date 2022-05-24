from django.db import models


class Article(models.Model):

    author = models.CharField(
        blank=True,
        max_length=255
    )

    sub = models.CharField(
        blank=True,
        max_length=255
    )

    content = models.TextField()

    is_published = models.BooleanField(
        default=True
    )

    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.sub


class Comment(models.Model):

    author = models.CharField(
        max_length=255
    )

    content = models.TextField()

    created_date = models.DateTimeField(
        auto_now_add=True
    )

