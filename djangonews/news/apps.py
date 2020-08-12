from django.apps import AppConfig


class NewsConfig(AppConfig):
    name = 'djangonews.news'

    # def ready(self):
    #     try:
    #         from . import signals
    #     except ImportError:
    #         pass
