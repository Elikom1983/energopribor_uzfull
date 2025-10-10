from tabnanny import verbose
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify


class Oferta(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_("Title")),
        description=RichTextField(verbose_name=_("Description")),  # ✅ CKEditor maydoni
    )

    seo_title = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("SEO Title"))
    seo_description = models.TextField(max_length=300, blank=True, null=True, verbose_name=_("SEO Description"))
    seo_keywords = models.CharField(max_length=200, blank=True, null=True, verbose_name=_("SEO Keywords"))

    def __str__(self):
        return self.safe_translation_getter('title', any_language=True)

    class Meta:
        verbose_name = _("Oferta")
        verbose_name_plural = _("Ofertas")
