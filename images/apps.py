from django.apps import AppConfig
from django.core.files import images


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'

    def ready(self):
        import images.signals