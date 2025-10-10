from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.html import format_html
from category.models import Category
from django.utils.text import slugify


# =======================
# Attributes
# =======================
# =======================
class Attribute(TranslatableModel):
    translations = TranslatedFields(
        name=models.CharField(max_length=200, verbose_name=_("Attribute Name"))
    )
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_("Slug"), blank=True)

    def __str__(self):
        return self.safe_translation_getter("name", any_language=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            name = self.safe_translation_getter("name", any_language=True)
            if name:
                self.slug = slugify(name)
        super().save(*args, **kwargs)


# =======================
# AttributeValue
# =======================
class AttributeValue(TranslatableModel):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name="values")
    translations = TranslatedFields(
        value=models.CharField(max_length=200, db_index=True, verbose_name=_("Value"))
    )

    def __str__(self):
        return f"{self.attribute}: {self.safe_translation_getter('value', any_language=True)}"


# =======================
# Product
# =======================
class Product(TranslatableModel):
    translations = TranslatedFields(
        product_name=models.CharField(max_length=200, unique=True, verbose_name=_('Product Name')),
        description=RichTextField(blank=True, verbose_name=_('Description')),
        short_description=models.TextField(max_length=330, blank=True, verbose_name=_('Short Description')),
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Title')),
    )
    meta = models.TextField(max_length=200, blank=True, null=True, verbose_name=_('Meta'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug'), blank=True)
    price = models.IntegerField(blank=True, null=True, verbose_name=_('Price'))
    discount = models.PositiveIntegerField(default=0, verbose_name=_('Discount (%)'))
    image = models.ImageField(upload_to='photos/products', verbose_name=_('Main Image'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    atribut_values = models.ManyToManyField(AttributeValue, blank=True, related_name='products', verbose_name=_('Attribute Values'))
    is_available = models.BooleanField(default=True, verbose_name=_('Available'))
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.safe_translation_getter("product_name", any_language=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            name = self.safe_translation_getter("product_name", any_language=True)
            if name:
                self.slug = slugify(name)
        super().save(*args, **kwargs)

    def discounted_price(self):
        if self.discount and self.price:
            return int(self.price - (self.price * self.discount / 100))
        return self.price

# =======================
# Product галерея
# =======================
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="gallery", verbose_name=_("Product"))
    image = models.ImageField(upload_to="photos/products/gallery", verbose_name=_("Gallery Image"))

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Gallery")

    def __str__(self):
        return f"{self.product} - Image"


# =======================
# Wishlist
# =======================
class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlisted_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user} → {self.product}"


# =======================
# Orders
# =======================
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    address_line = models.CharField(max_length=150)
    delivery_type = models.CharField(max_length=50, choices=[
        ('kuryer', 'Kuryer orqali'),
        ('olib ketish', 'O‘zim olib ketaman')
    ])
    payment_method = models.CharField(max_length=50, choices=[
        ('naqd', 'Naqd to‘lov'),
        ('online', 'Online to‘lov (Payme/Click)'),
        ('transfer', 'Pul o‘tkazish (bank orqali)')
    ])
    comment = models.TextField(blank=True, null=True)
    total_price = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    transfer_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="O‘tkazilgan summa")
    transfer_receipt = models.ImageField(upload_to='transfers/', blank=True, null=True, verbose_name="To‘lov cheki (rasm)")
    resolved = models.BooleanField(default=False)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} - {self.phone}"

    def ordered_items(self):
        result = ""
        for item in self.items.all():
            result += "<label class='required'>{}:</label>".format(item.product.product_name)
            result += "<p class='file-upload'>{}</p>".format(item.quantity)
            result += "<br/>"
        return format_html(result)

    ordered_items.allow_tags = True


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, related_name="items")
    quantity = models.IntegerField()

    def __str__(self):
        return str(self.product)
    


# =======================
# MetaWords
# =======================
class MetaWords(models.Model):
    meta = models.CharField(max_length=255, verbose_name=_('Meta'))

    def __str__(self):
        return str(self.meta)

    class Meta:
        verbose_name = 'Meta Word'
        verbose_name_plural = 'Meta Words'
