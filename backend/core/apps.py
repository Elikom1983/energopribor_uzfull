from django.apps import AppConfig

class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

    def ready(self):
        # admin ҳам кўра олиши учун фильтрни импорт қиламиз
        import core.templatetags.custom_filters
