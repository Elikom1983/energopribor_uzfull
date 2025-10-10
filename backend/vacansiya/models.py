from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField


class Vacansiya(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_("Сарлавха")),
        content=RichTextField(verbose_name=_("Контент")),  # ✅ to‘g‘risi shu
    )

    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Title"))
    seo_description = models.TextField(blank=True, null=True, verbose_name=_("SEO Description"))
    seo_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Keywords"))

    class Meta:
        verbose_name = _("Vacansiya")
        verbose_name_plural = _("Vacansiyalar")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Vacansiya"


class VacansiyaItem(TranslatableModel):  # ✅ Nomini aniqroq qildim
    vacansiya = models.ForeignKey(
        Vacansiya,
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("Asosiy Vacansiya")
    )
    translations = TranslatedFields(
        position=models.CharField(max_length=255, verbose_name=_("Lavozim nomi")),  # ✅
    )

    class Meta:
        verbose_name = _("Vacansiya item")
        verbose_name_plural = _("Vacansiya itemlar")

    def __str__(self):
        return self.safe_translation_getter("position", any_language=True) or "Vakansiya item"
