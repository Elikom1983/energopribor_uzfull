from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField


class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_("Сарлавҳа")),
        description=models.TextField(verbose_name=_("Қисқача матн")),
        content=RichTextField(verbose_name=_("Контент")),
        slug=models.SlugField(max_length=255, unique=True, blank=True, null=True, verbose_name=_("Slug"))
    )

    image = models.ImageField(upload_to="news/", verbose_name=_("Расм"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 🔑 SEO майдонлар
    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Title"))
    seo_description = models.TextField(blank=True, null=True, verbose_name=_("SEO Description"))
    seo_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Keywords"))

    class Meta:
        verbose_name = _("Янгилик")
        verbose_name_plural = _("Янгиликлар")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True)

    def save(self, *args, **kwargs):
        if not self.safe_translation_getter("slug", any_language=False):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("news_detail", kwargs={"slug": self.slug})
