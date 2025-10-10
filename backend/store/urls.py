from . import  views
from django.urls import path
from django.conf.urls import handler404, handler500
from .views import AttributeValueAutocomplete
app_name = 'store'  # 🔹 MUHIM! Namespace uchun shart


urlpatterns = [
    path('attribute-values-autocomplete/', AttributeValueAutocomplete.as_view(), name='attribute-values-autocomplete'),
    path('', views.store, name='store'),
    path('category/<slug:category_slug>/', views.store, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('catalog/', views.store_category, name='store_category'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete/', views.complete, name='complete'),
    path('search/', views.search, name='search'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/toggle/<int:product_id>/', views.toggle_wishlist, name='toggle_wishlist'),
    path('wishlist/clear/', views.clear_wishlist, name='clear_wishlist'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/update/', views.update_cart, name='update_cart'),
    path('cart/remove_item/', views.remove_cart_item, name='remove_cart_item'),
    path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('ajax/filter-products/', views.ajax_filter_products, name='ajax_filter_products'),
     
]