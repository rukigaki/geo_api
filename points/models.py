from django.contrib.gis.db import models
from django.contrib.auth.models import User


class Point(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="points"
    )

    location = models.PointField(
        geography=True,
        srid=4326
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Point #{self.id}"


class Message(models.Model):
    point = models.ForeignKey(
        "Point",
        related_name="messages",
        on_delete=models.CASCADE,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="messages"
    )

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message #{self.id} by {self.author.username}"
