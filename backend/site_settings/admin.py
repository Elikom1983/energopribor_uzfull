from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Footeraddres,SiteSettings,Socials,PaymentMethod
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'phone_number', 'logo')

@admin.register(Footeraddres)
class FooteraddresAdmin(TranslatableAdmin):
    list_display = ("get_address", "get_telefon", "get_email")

    def get_address(self, obj):
        return obj.safe_translation_getter("address", any_language=True)
    get_address.short_description = "Manzil"

    def get_telefon(self, obj):
        return obj.safe_translation_getter("telefon", any_language=True)
    get_telefon.short_description = "Telefon"

    def get_email(self, obj):
        return obj.safe_translation_getter("email", any_language=True)
    get_email.short_description = "Email"

    # faqat 1 marta qo'shish uchun
    def has_add_permission(self, request):
        if Footeraddres.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return False
@admin.register(Socials)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'classlink')

@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo', 'link')
    
