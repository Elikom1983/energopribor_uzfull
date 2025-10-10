from django.contrib import admin
from parler.admin import TranslatableAdmin, TranslatableTabularInline
from .models import Vacansiya, VacansiyaItem
from ckeditor.widgets import CKEditorWidget
from django.db import models


class VacansiyaItemInline(TranslatableTabularInline):  # ✅ nomi to‘g‘rilandi
    model = VacansiyaItem
    extra = 1
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


@admin.register(Vacansiya)
class VacansiyaAdmin(TranslatableAdmin):  # ✅ nomi ham to‘g‘rilandi
    list_display = ('title_display',)
    inlines = [VacansiyaItemInline]

    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
        ("SEO", {
            'fields': ('seo_title', 'seo_description', 'seo_keywords')
        }),
    )

    @admin.display(description="Сарлавҳа")
    def title_display(self, obj):
        return obj.safe_translation_getter("title", any_language=True)


@admin.register(VacansiyaItem)
class VacansiyaItemAdmin(TranslatableAdmin):
    list_display = ("position_display", "vacansiya")  # ✅ faq emas, vacansiya

    fieldsets = (
        (None, {
            'fields': ('vacansiya', 'position')  # ✅ position qo‘shildi
        }),
    )

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

    @admin.display(description="Lavozim")
    def position_display(self, obj):
        return obj.safe_translation_getter("position", any_language=True)
