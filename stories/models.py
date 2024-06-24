from django.db import models
from datetime import timedelta
from rest_framework.fields import uuid

from organization.models import Organization


# Create your models here.
class Story(models.Model):
    """The story model represents a story in academia"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
    )

    hex_code = models.CharField(
        max_length=7,
        blank=False,
        null=True,
        default="3698cf",
    )

    text = models.TextField()

    media = models.FileField(
        upload_to="stories-media/",
        blank=True,
        null=True,
    )

    # date added
    date_added = models.DateTimeField(
        auto_created=True,
    )

    # date of expiry
    date_of_expiry = models.DateTimeField(
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if not self.date_of_expiry:
            self.date_of_expiry = self.date_added + timedelta(hours=24)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.id} - {self.text[:10]}"
