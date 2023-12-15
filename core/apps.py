""" Imports """
from django.apps import AppConfig


""" Setting """
class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
    label = "core"
