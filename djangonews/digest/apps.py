from django.apps import AppConfig


class DigestConfig(AppConfig):
    name = 'djangonews.digest'

    def ready(self):
        from . import receivers
