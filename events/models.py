from django.db import models
import uuid
import mimetypes


class Event(models.Model):
    """
    Represents an event thrown by multiple parties
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # event name
    name = models.CharField(
        max_length=60,
        blank=False,
    )

    # event contacts
    phone = models.CharField(
        max_length=10,
        blank=False,
    )

    # event email
    email = models.EmailField(
        blank=False,
        null=False,
    )

    # event location
    location = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    likes = models.IntegerField(
        default=0,
    )

    # brief description
    description = models.TextField(
        blank=True,
        null=True,
    )

    # event poster or video
    media = models.FileField(
        upload_to="events-media/",
    )

    media_type = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    url = models.URLField(
        blank=True,
        null=True,
    )

    # start date
    start_date = models.DateTimeField(
        blank=False,
        null=False,
    )

    end_date = models.DateTimeField(
        blank=False,
        null=False,
    )

    # date added
    date_added = models.DateTimeField(
        auto_created=True,
    )

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        self.media_type = mimetypes.guess_type(self.media.path)[0]
        self.likes = 0
        super().save(*args, **kwargs)


class EventLike(models.Model):
    """A class that represents an event's like transaction"""

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="event_likes",
    )
    user = models.CharField(
        max_length=60,
    )
    liked_at = models.DateField(auto_now_add=True)
    attending = models.BooleanField(default=False)

    def __str__(self) -> str:
        """Returns a string representation of the model"""

        return f"{self.user} likes {self.event.name}"
