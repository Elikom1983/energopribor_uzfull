from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from ckeditor.fields import RichTextField


class About(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=255, verbose_name=_("Сарлавҳа")),        
        content=RichTextField(verbose_name=_("Контент")),
    )

    
    imagevideo = models.ImageField(
    upload_to="about/",
    blank=True,
    null=True,
    verbose_name=_("video rasmi")
)

    video=models.CharField(max_length=255, verbose_name="video silkasini qoying")
    banerimg = models.ImageField(
    upload_to="about/",
    blank=True,
    null=True,
    verbose_name=_("banner rasmi")
)

    seo_title = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Title"))
    seo_description = models.TextField(blank=True, null=True, verbose_name=_("SEO Description"))
    seo_keywords = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("SEO Keywords"))

    class Meta:
        verbose_name = _("Biz haqimizda")
        verbose_name_plural = _("Biz haqimizda")

    def __str__(self):
        return self.safe_translation_getter("title", any_language=True) or "Biz haqimizda"
    
class Aboutnumber(TranslatableModel):
    translations = TranslatedFields(
        raqamlar=models.CharField(max_length=255, verbose_name=_("Сарлавҳа")),
        text=models.CharField(max_length=255, verbose_name=_("Текст")),        
       
    )
    class Meta:
         verbose_name = _("Malumotlar")
         verbose_name_plural = _("Kompaniyamiz raqamlarda")
    def __str__(self):
        return self.safe_translation_getter("raqamlar", any_language=True) or "Kompaniyamiz raqamlarda"
class Team(TranslatableModel):
    translations = TranslatedFields(
        ismi=models.CharField(max_length=255, verbose_name=_("Ismi")),
        lavozimi=models.CharField(max_length=255, verbose_name=_("Lavozimi")),
    )
    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True,
        verbose_name=_("Hodim rasmi")
    )

    class Meta:
        verbose_name = _("Bizning jamoa")
        verbose_name_plural = _("Hodimlar")

    def __str__(self):
        return self.safe_translation_getter("ismi", any_language=True) or "Hodim"
    
class Yutuqlar(models.Model):
    image = models.ImageField(
        upload_to="about/",
        blank=True,
        null=True,
        verbose_name=_("Yutuqlar rasmi")
    )

    def __str__(self):
        return str(('image'))

    class Meta:
        verbose_name = 'Bizning yutuqlar'
        verbose_name_plural = 'Yutuqlar'





