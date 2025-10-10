from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Contact
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.utils.safestring import mark_safe


@admin.register(Contact)
class ContactAdmin(TranslatableAdmin):
    list_display = ('title_display',)  # vergul қўшилди
   

    fieldsets = (
        (None, {
            'fields': ('title', 'image', 'adress', 'phone','email','map')  # vergul тўғриланди
        }),
        ("SEO", {
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},  # content учун CKEditor
    }

    @admin.display(description="Сарлавҳа")
    def title_display(self, obj):
        return obj.safe_translation_getter("title", any_language=True)
