from django.contrib.auth.models import User

# Create your models here.

from django.db import models
from store.models import Product


# Create your models here.

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)  # null=False bo‘lishi yaxshiroq
    quantity = models.PositiveIntegerField(default=1)  # default 1 qo‘shish
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product} ({self.quantity})"


    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product