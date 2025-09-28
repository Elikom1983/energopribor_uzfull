from django.db import models
from category.models import Category
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.utils.html import format_html
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.conf import settings   # 🔹 BU QATORNI QO‘SHISH SHART


class Product(TranslatableModel):
    translations = TranslatedFields(
        product_name=models.CharField(max_length=200, unique=True, verbose_name=_('Product Name')),
        description=RichTextField(blank=True, verbose_name=_('Description')),
        short_description = models.TextField(max_length=330, blank=True, verbose_name=_('Short Description')),
        title=models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Title')),
    )
    meta = models.TextField(max_length=200, blank=True, null=True, verbose_name=_('Meta'))
    slug = models.SlugField(max_length=200, unique=True, verbose_name=_('Slug'))
    price = models.IntegerField(blank=True, null=True,verbose_name=_('Price'))
    image = models.ImageField(upload_to='photos/products', verbose_name=_('Images'))
    is_available = models.BooleanField(default=True, verbose_name=_('Is Available'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_('Category'))
    top = models.BooleanField(default=False, verbose_name=_('Top'))
    new = models.BooleanField(default=False, verbose_name=_('New'))
    v_nalichi = models.BooleanField(default=True, verbose_name=_('V nalichii'))
    cena_po_zaprosu = models.BooleanField(default=False, verbose_name=_('Price po zaprosu'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=_('Created Date'))
    modified_date = models.DateTimeField(auto_now=True, verbose_name=_('Modified Date'))

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

class Wishlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlisted_by")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'product')  # bir foydalanuvchi bitta mahsulotni ikki marta qo‘sha olmaydi

    def __str__(self):
        return f"{self.user} -> {self.product}"
    
class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    address_line = models.CharField(max_length=50)

    resolved = models.BooleanField(default=False)

    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.phone)
    

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


class MetaWords(models.Model):
    meta = models.CharField(max_length=255, verbose_name=_('meta'))

    def __str__(self):
        return str(self.meta)

    class Meta:
        verbose_name = 'Meta Word'
        verbose_name_plural = 'Meta Words'