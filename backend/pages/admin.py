from django.contrib import admin
from .models import *
from parler import admin as parler_admin
from parler.admin import TranslatableAdmin
from django.utils.safestring import mark_safe


# Register your models here.

class AboutAdmin(TranslatableAdmin):
    list_display = ('title',)


admin.site.register(AboutImages, AboutAdmin)


class AboutMainAdmin(admin.ModelAdmin):
    pass



admin.site.register(AboutMainImage, AboutMainAdmin)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')


admin.site.register(Brand, BrandAdmin)

class PartnersAdmin(admin.ModelAdmin):
    list_display = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')


admin.site.register(Partners, PartnersAdmin)



@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag')  # Админда расм чиқади


@admin.register(Banner)
class Banner(TranslatableAdmin):
    pass


@admin.register(Bannerhome)
class BannerhomeAdmin(TranslatableAdmin):
    list_display = ('title', 'image')
    
    # Faqat bitta object bo‘lishi uchun
    def has_add_permission(self, request):
        if Bannerhome.objects.exists():
            return False
        return super().has_add_permission(request)
    
@admin.register(Bannerfoter)
class Bannerfoteradmin(TranslatableAdmin):
    list_display = ('title', 'text')  # = белгисини унутманг!

    def has_add_permission(self, request):
        if Bannerfoter.objects.exists():
            return False
        return super().has_add_permission(request)
@admin.register(HomeSeo)
class HomeSeoAdmin(TranslatableAdmin):
    list_display = ('title', 'description', 'keywords')  # = белгисини унутманг!

    def has_add_permission(self, request):
        if HomeSeo.objects.exists():
            return False
        return super().has_add_permission(request)
