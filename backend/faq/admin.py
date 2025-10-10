from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline
from .models import Faq, FaqItem
from ckeditor.widgets import CKEditorWidget
from django.db import models

class FaqItemInline(TranslatableTabularInline):
    model = FaqItem
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

@admin.register(Faq)
class FaqAdmin(TranslatableAdmin):
    list_display = ('title_display',)
    inlines = [FaqItemInline]

    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        ("SEO", {
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        }),
    )

    @admin.display(description="Сарлавҳа")
    def title_display(self, obj):
        return obj.safe_translation_getter("title", any_language=True)

@admin.register(FaqItem)
class FaqItemAdmin(TranslatableAdmin):
    list_display = ("question_display", "faq")

    fieldsets = (
        (None, {
            'fields': ('faq', 'question', 'answer')
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

    @admin.display(description="Савол")
    def question_display(self, obj):
        return obj.safe_translation_getter("question", any_language=True)
