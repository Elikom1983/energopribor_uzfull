from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields

class Faq(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_("FAQ категория номи")),        
    )

    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Title"))
    seo_description = models.TextField(blank=True, null=True, verbose_name=_("SEO Description"))
    seo_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Keywords"))

    class Meta:
        verbose_name = _("FAQ sahifasi")
        verbose_name_plural = _("FAQ sahifasi")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "FAQ категорияси"

class FaqItem(TranslatableModel):
    faq = models.ForeignKey(Faq, on_delete=models.CASCADE, related_name="questions")
    translations = TranslatedFields(
        question=models.CharField(max_length=255, verbose_name=_("Савол")),
        answer=models.TextField(verbose_name=_("Жавоб")),       
    )

    class Meta:
        verbose_name = _("FAQ савол-жавоб")
        verbose_name_plural = _("FAQ савол-жавоблар")

    def __str__(self):
        return self.safe_translation_getter("question", any_language=True) or "FAQ савол"
