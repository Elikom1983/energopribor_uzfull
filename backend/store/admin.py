from django.contrib import admin
from django.utils.safestring import mark_safe
from parler.admin import TranslatableAdmin
from .models import (
    Product, ProductImage,
    Attribute, AttributeValue,
    Wishlist, Order, OrderItem, MetaWords
)



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ('image',)
    verbose_name = "Qo‘shimcha rasm"
    verbose_name_plural = "Galereya rasmlari"

    
    def preview_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60" height="60" style="border-radius:5px;object-fit:cover;" />')
        return "-"
    preview_image.short_description = "Oldindan ko'rish"

@admin.register(Product)
class ProductAdmin(TranslatableAdmin):
    list_display = ('get_image', 'get_name', 'price', 'discount', 'is_available', 'created_date')
    search_fields = ('translations__product_name',)
    list_filter = ('price', 'discount', 'is_available')
    list_per_page = 15
    inlines = [ProductImageInline]
    filter_vertical = ('atribut_values',)

    fieldsets = (
        (None, {
            'fields': ('product_name', 'slug', 'price', 'discount', 'image',
                       'short_description', 'description', 'atribut_values', 'is_available')
        }),
    )

    def get_name(self, obj):
        return obj.safe_translation_getter("product_name", any_language=True)
    get_name.short_description = "Mahsulot nomi"

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60" height="60" style="border-radius:5px;object-fit:cover;" />')
        return "-"
    get_image.short_description = "Rasm"
    
@admin.register(Attribute)
class AttributeAdmin(TranslatableAdmin):
    list_display = ('get_name', 'slug')
    search_fields = ('translations__name',)

    def get_name(self, obj):
        return obj.safe_translation_getter("name", any_language=True)
    get_name.short_description = "Attribute nomi"

@admin.register(AttributeValue)
class AttributeValueAdmin(TranslatableAdmin):
    list_display = ('get_value', 'get_attribute')
    search_fields = ('translations__value',)

    def get_value(self, obj):
        return obj.safe_translation_getter("value", any_language=True)
    def get_attribute(self, obj):
        return obj.attribute.safe_translation_getter("name", any_language=True)

    get_value.short_description = "Qiymat"
    get_attribute.short_description = "Attribute"

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'total_price', 'resolved', 'date_added')
    list_filter = ('resolved', 'delivery_type', 'payment_method', 'date_added')
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    readonly_fields = ('date_added', 'ordered_items')
    fieldsets = (
        ("Buyurtma ma'lumotlari", {
            'fields': ('first_name', 'last_name', 'phone', 'email', 'address_line')
        }),
        ("Yetkazib berish va to'lov", {
            'fields': ('delivery_type', 'payment_method', 'total_price', 'transfer_amount', 'transfer_receipt')
        }),
        ("Qo'shimcha", {
            'fields': ('message', 'comment', 'resolved', 'ordered_items', 'date_added')
        }),
    )

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity')
    list_filter = ('order',)

admin.site.register(Wishlist)
admin.site.register(MetaWords)
# ProductImage inline orqali ko'rsatiladi