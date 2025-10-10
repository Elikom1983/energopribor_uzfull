from django.contrib import admin
from django.utils.text import slugify
from mptt.admin import MPTTModelAdmin
from parler.admin import TranslatableAdmin
from .models import Category, MetaDetail


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin, MPTTModelAdmin):
    mptt_level_indent = 50
    search_fields = ('translations__name',)
    ordering = ['id']
    list_display = ('translated_name', 'slug', 'parent')

    def save_model(self, request, obj, form, change):
        name = obj.safe_translation_getter('name', any_language=True)
        if not obj.slug and name:
            obj.slug = slugify(name)
        super().save_model(request, obj, form, change)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}


@admin.register(MetaDetail)
class MetaAdmin(admin.ModelAdmin):
    list_display = ['category', 'keyword', 'description']
    list_display_links = ['category', 'keyword']
