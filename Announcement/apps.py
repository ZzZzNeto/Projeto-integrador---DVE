from django.apps import AppConfig

class AnnouncementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Announcement'
        
    def ready(self):
        from .Jobs import updater
        updater.start()
        