from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import News
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.utils.safestring import mark_safe

        

class NewsAdmin(TranslatableAdmin):
    list_display = ('get_image','title')
    search_fields = ('title','description','content', 'slug')
    fieldsets = (
        (None, {
            'fields': ('title','description','content', 'slug','image','seo_title','seo_description','seo_keywords'),
        }),
    )
    list_per_page = 15

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('title',)
        }

admin.site.register(News, NewsAdmin)
