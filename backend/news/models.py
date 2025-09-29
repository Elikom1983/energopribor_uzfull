from django.db import models
from category.models import Category
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from django.utils.html import format_html
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.conf import settings  


class News(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_("Сарлавҳа")),
        description=models.TextField(verbose_name=_("Қисқача матн")),
        content=RichTextField(verbose_name=_("Контент")),
    )

    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("Slug"), blank=True)  # slug blank=True bo‘lishi kerak
    image = models.ImageField(upload_to="news/", verbose_name=_("Расм"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # SEO maydonlar
    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Title"))
    seo_description = models.TextField(blank=True, null=True, verbose_name=_("SEO Description"))
    seo_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Keywords"))

    class Meta:
        verbose_name = _("Янгилик")
        verbose_name_plural = _("Янгиликлар")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Yangilik"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.safe_translation_getter("title", any_language=True))
            slug = base_slug
            counter = 1
            while News.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("news_detail", kwargs={"slug": self.slug})
