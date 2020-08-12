import uuid

from djangonews.core.utils.models import TimeStampedModel
from django.conf import settings
from django.db import models

USER = settings.AUTH_USER_MODEL


class Letter(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frequency = models.CharField(
        max_length=16, choices=(("weekly", "weekly"), ("daily", "daily"))
    )
    weekly_weekday = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        choices=(
            ("Sun", "Sun"),
            ("Mon", "Mon"),
            ("Tue", "Tue"),
            ("Wed", "Wed"),
            ("Thu", "Thu"),
            ("Fri", "Fri"),
            ("Sat", "Sat"),
        ),
    )
    stories = models.ManyToManyField("news.Story")


class Subscription(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    frequency = models.CharField(
        max_length=16, choices=(("weekly", "weekly"), ("daily", "daily"))
    )
    weekly_weekday = models.CharField(
        max_length=16,
        null=True,
        blank=True,
        choices=(
            ("Sun", "Sun"),
            ("Mon", "Mon"),
            ("Tue", "Tue"),
            ("Wed", "Wed"),
            ("Thu", "Thu"),
            ("Fri", "Fri"),
            ("Sat", "Sat"),
        ),
    )
    verfied_email = models.EmailField(null=True, blank=True)
    is_active = models.BooleanField(default=False)


class UserSubscription(Subscription):
    user = models.ForeignKey(to=USER, on_delete=models.CASCADE, null=True)


class AnonymousSubscription(Subscription):
    email = models.EmailField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    verified_at = models.DateTimeField(null=True)
    verification_code = models.UUIDField(
        primary_key=False, default=uuid.uuid4, editable=False
    )
    logged_in_user = models.ForeignKey(to=USER, on_delete=models.CASCADE, null=True)


class UnSubscription(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    from_digests = models.ForeignKey(Letter, on_delete=models.CASCADE, null=True)
