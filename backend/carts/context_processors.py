from .models import Cart, CartItem
from .views import _cart_id


def counter(request):
    cart_count = 0
    try:
        cart = Cart.objects.filter(cart_id=_cart_id(request), is_active=True)
        cart_items = CartItem.objects.filter(cart=cart.first(), is_active=True)
        for cart_item in cart_items:
            cart_count += cart_item.quantity
    except Cart.DoesNotExist:
        cart_count = 0
    return dict(cart_count=cart_count)
