from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import About,Aboutnumber,Team,Yutuqlar
from ckeditor.widgets import CKEditorWidget
from django.db import models
from django.utils.safestring import mark_safe


@admin.register(About)
class AboutAdmin(TranslatableAdmin):
    list_display = ('title_display',)  # vergul қўшилди
   

    fieldsets = (
        (None, {
            'fields': ('title', 'imagevideo', 'video', 'content', 'banerimg')  # vergul тўғриланди
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
@admin.register(Aboutnumber)
class AboutnumberAdmin(TranslatableAdmin):
     list_display = ('raqamlar','text')      
     fieldsets = (
            (None, {
                'fields': ('raqamlar','text')  # vergul тўғриланди
            }),
           
        )
@admin.register(Team)
class TeamAdmin(TranslatableAdmin):
    list_display = ('get_name', 'get_position', 'get_image')

    fieldsets = (
        (None, {
            'fields': ('image', 'ismi', 'lavozimi')
        }),
    )

    @admin.display(description="Ismi")
    def get_name(self, obj):
        return obj.safe_translation_getter("ismi", any_language=True)

    @admin.display(description="Lavozimi")
    def get_position(self, obj):
        return obj.safe_translation_getter("lavozimi", any_language=True)

    @admin.display(description="Rasm")
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')

@admin.register(Yutuqlar)
class YutuqlarAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="auto" height="60" />')
        return "-"
    get_image.short_description = "Рисунок"


