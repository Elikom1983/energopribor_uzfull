from django.contrib import admin
from parler.admin import TranslatableAdmin
from django.utils.safestring import mark_safe
from store.models import Product, Order, OrderItem, MetaWords


class ProductAdmin(TranslatableAdmin):
    list_display = ('get_image', 'product_name', 'title', 'meta','price', 'category', 'modified_date', 'is_available')
    search_fields = ('translations__product_name',)
    fieldsets = (
        (None, {
            'fields': ('product_name', 'title','slug', 'meta','category', 'image', 'price', 'short_description','description', 'top', 'new', 'cena_po_zaprosu','v_nalichi', 'is_available'),
        }),
    )
    list_per_page = 15

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="auto" height="60"')

    def get_prepopulated_fields(self, request, obj=None):
        return {
            'slug': ('product_name',)
        }

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['first_name', 'last_name', 'phone', 'email', 'message', 'address_line', 'ordered_items'] 
    list_display = ['fullname', 'phone', 'email', 'resolved',]
    list_filter = ['resolved',]
    search_fields = ['first_name', 'last_name', 'phone', 'email']
    list_per_page = 20

    def fullname(self, obj=None):
        return "{} {}".format(obj.first_name, obj.last_name)
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Order, OrderAdmin)
admin.site.register(MetaWords)
# class OrderItemAdmin(admin.ModelAdmin):
#     readonly_fields = ['product', 'order', 'quantity']
#     list_display = ['id', 'product', 'order', 'quantity']
#     list_per_page = 20

# admin.site.register(OrderItem, OrderItemAdmin)
