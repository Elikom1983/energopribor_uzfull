from django.contrib import admin
from .models import Category, MetaDetail
from parler.admin import TranslatableAdmin
from mptt.admin import MPTTModelAdmin


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin, MPTTModelAdmin):
    mptt_level_indent = 50
    search_fields = ('translations__name',)
    ordering = ['id']

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('name',)
        }


class MetaAdmin(admin.ModelAdmin):
    list_display = ['category', 'keyword', 'description']
    
    list_display_links = ['category', 'keyword']

    class Meta:
        model = MetaDetail
    
admin.site.register(MetaDetail, MetaAdmin)
