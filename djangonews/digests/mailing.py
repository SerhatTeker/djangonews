from django.conf import settings
from .models import Subscription, Letter


def create_and_send_digests(frequency):
    pass
    # Get list of objects
    stories = []  # TODO: Find from _font_page
    # make templates and trigger sending
    subscriptions = Subscription.objects.filter(is_active=True, frequency=frequency)
    for subscription in subscriptions:
        tpl = "TODO: Here is your list"  # TODO
        subject = settings.SITE_NAME + " " + frequency + " Letter"
        send_mail(subscription, tpl, subject)


def send_mail(subscription, template, subject):
    pass
