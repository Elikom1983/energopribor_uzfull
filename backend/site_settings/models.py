from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class SiteSettings(models.Model):
    site_name = models.CharField("Сайт номи", max_length=255, blank=True)
    # logo = models.ImageField("Лого", upload_to="logos/", blank=True, null=True)
    logo = models.FileField("Лого (SVG ёки PNG)", upload_to="logos/", blank=True, null=True)
    phone_number = models.CharField("Телефон рақами", max_length=20, blank=True)

    def __str__(self):
        return self.site_name or "Телефон ёки лого жойлаш"



class Footeraddres(TranslatableModel):
    translations = TranslatedFields(
        address=models.CharField(max_length=200, verbose_name=_('Korxona manzili')),
        telefon=models.CharField(max_length=200, verbose_name=_('Telefon raqami')),
        email=models.CharField(max_length=200, verbose_name=_('Email manzili'))
    )

    def __str__(self):
        return self.safe_translation_getter("address", any_language=True) or "Footer address"
from django.db import models
from django.utils.translation import gettext_lazy as _


class Socials(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Nomi'))
    link = models.URLField(max_length=200, verbose_name=_('Havola'))
    classlink = models.CharField(max_length=200, verbose_name=_('CSS klassi'))  # масалан: "fa fa-facebook"

    class Meta:
        verbose_name = "Social tarmoq"
        verbose_name_plural = "Social tarmoqlar"

    def __str__(self):
        return self.title
class PaymentMethod(models.Model):
    title = models.CharField(max_length=200, verbose_name=_('Nomi'))  # Masalan: Payme
    logo = models.ImageField(upload_to="payments/", verbose_name=_('Rasm'))  # Masalan: Payme logosi
    link = models.URLField(blank=True, null=True, verbose_name=_('Toʻlov ssilkasi'))  # ixtiyoriy

    class Meta:
        verbose_name = "Toʻlov usuli"
        verbose_name_plural = "Toʻlov usullari"

    def __str__(self):
        return self.title




    

