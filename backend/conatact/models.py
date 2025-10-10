from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
class Contact(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(max_length=200, verbose_name=_('Sarlavha')),
        adress = models.CharField(max_length=255, default="Manzil mavjud emas", verbose_name=_('Adress')),
    )

    phone = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Telefon'))
    email = models.EmailField(blank=True, null=True, verbose_name=_('Pochta'))
    image = models.ImageField(upload_to='photos/banners', verbose_name="Banner rasmi")
    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Title"))
    seo_description = models.TextField(blank=True, null=True, verbose_name=_("SEO Description"))
    seo_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Keywords"))
    map = models.TextField(verbose_name="Karta joylang")
    class Meta:
        verbose_name = _("Biz bilan bog‘lanish")
        verbose_name_plural = _("Biz bilan bog‘lanish")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Biz bilan bog‘lanish"

  


