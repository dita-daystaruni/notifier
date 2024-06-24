from django.db import models
import uuid


# Create your models here.
class Organization(models.Model):
    """The organization model represents the various organizations in the school."""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # organization name
    name = models.CharField(
        max_length=60,
        blank=False,
    )

    # organization contacts
    phone = models.CharField(
        max_length=10,
        blank=False,
    )

    # organization email
    email = models.EmailField(
        blank=False,
        null=False,
    )

    # organization profile picture
    profile = models.ImageField(
        upload_to="profiles/",
    )

    # date added
    date_added = models.DateTimeField(
        auto_created=True,
    )
