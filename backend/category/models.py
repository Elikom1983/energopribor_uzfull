from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from .managers import CategoryManager
from django.urls import reverse

class MetaDetail(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE, blank=True, null=True)
    keyword = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return str(self.category)

    class Meta:
        verbose_name = 'Meta'

class Category(MPTTModel, TranslatableModel):
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
        verbose_name=_('Parent')
    )
    translations = TranslatedFields(
        name=models.CharField(max_length=255, verbose_name=_('Name'), null=True, blank=True),
    )
    slug = models.CharField(max_length=255, null=True, blank=True, verbose_name=_('Slug'))
    image = models.ImageField(upload_to='images/category', default='category/default.jpg', verbose_name=_('Images'))
    is_popular = models.BooleanField(default=False, verbose_name="Ommabop kategoriya")

    objects = CategoryManager()

    class Meta:
        verbose_name = _('Categoriya')
        verbose_name_plural = _('Categorialar')

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.translated_name

    @property
    def translated_name(self):
        return self.safe_translation_getter("name", any_language=True) or "-"

    # 🔹 Тўғри URL
    def get_absolute_url(self):
        return reverse('products_by_category', kwargs={'category_slug': self.slug})
