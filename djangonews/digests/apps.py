from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DigestsConfig(AppConfig):
    name = "djangonews.digests"
    verbose_name = _("Digests")
