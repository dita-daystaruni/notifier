import uuid
from django.db import models
from rest_framework.generics import ValidationError


# Create your models here.
class Semester(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    # semester name
    name = models.CharField(
        max_length=60,
        blank=False,
    )

    # semester code
    code = models.CharField(
        max_length=60,
        blank=False,
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


class SemesterEvent(models.Model):

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE,
        related_name="semester_events",
    )

    # semester name
    name = models.CharField(
        max_length=60,
        blank=False,
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

    def clean(self):
        super().clean()
        if (
            self.start_date < self.semester.start_date
            or self.end_date > self.semester.end_date
        ):
            raise ValidationError(
                "Semester event dates must be within the semester's start and end dates."
            )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
