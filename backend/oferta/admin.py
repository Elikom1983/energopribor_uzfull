from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Oferta


@admin.register(Oferta)
class OfertaAdmin(TranslatableAdmin):
    list_display = ('get_title',)
    search_fields = ('translations__title',)

    fieldsets = (
        (None, {
            'fields': ('title', 'description'),
        }),
        ('SEO Settings', {
            'fields': ('seo_title', 'seo_description', 'seo_keywords'),
        }),
    )

    def get_title(self, obj):
        return obj.safe_translation_getter('title', any_language=True)

    get_title.short_description = "Title"
