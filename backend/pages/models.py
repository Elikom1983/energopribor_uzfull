from django.db import models
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField



# Create your models here.
class Banner(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
    )
    image = models.ImageField(upload_to='photos/banners')
    link = models.URLField(blank=True, null=True)
    colorbutton = ColorField(default='#FFFFFF', blank=True, null=True)
    backgrouncolor=ColorField(default='#FFFFFF', blank=True, null=True)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Slider'
        verbose_name_plural = 'Sliderlar'
class HomeSeo(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
        description=models.TextField(blank=True, verbose_name=_('Description')),
        keywords=models.TextField(max_length=300, blank=True, verbose_name=_('Keywords')),
    )

    def save(self, *args, **kwargs):
        if not self.pk and HomeSeo.objects.exists():
            # Agar объект аллақачон бор бўлса, янги объект қўшилмайди
            raise Exception('Фақат битта HomeSeo объекти бўлиши мумкин!')
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.safe_translation_getter("title", any_language=True) or "HomeSeo")

    class Meta:
        verbose_name = 'Home Seo'
        verbose_name_plural = 'Home Seo'


class Brand(models.Model):
    image = models.ImageField(upload_to='photos/brands')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


from django.db import models
from django.utils.html import format_html

class Clients(models.Model):  
    image = models.ImageField(upload_to='photos/clients')

    def __str__(self):
        return f"Client {self.id}"  # Админда ном кўринади

    # Админда расм кўрсатиш
    def image_tag(self):
        if self.image:
            return format_html('<img src="{}" width="100" />', self.image.url)
        return "No Image"
    image_tag.short_description = 'Image'

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'



class AboutMainImage(models.Model):
    main_image = models.ImageField(upload_to='photos/about', verbose_name=_('Main Image'))

    def __str__(self):
        return str(('image'))

    class Meta:
        verbose_name = 'About Main Image'
        verbose_name_plural = 'About Main Image'

class AboutImages(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, verbose_name=_('Title')),
        description=models.TextField(max_length=200, verbose_name=_('Description')),
    )
    image = models.ImageField(upload_to='photos/about', blank=True, null=True, verbose_name=_('Image'))
    

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'


class Partners(models.Model):
    image = models.ImageField(upload_to='photos/about', verbose_name=_('Image 1'))
    url = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Link'))

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'

class Team(TranslatableModel):
    translations = TranslatedFields(
        name = models.CharField(max_length=250, verbose_name=_('Name')),
        position = models.CharField(max_length=250, verbose_name=_('Position')),
        email = models.CharField(max_length=250, verbose_name=_('Email')),
    )

    image = models.ImageField(upload_to='photos/about', verbose_name=_('Image 1'))
    phone = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Phone'))
    telegram = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Telegram'))
    instagram = models.CharField(max_length=250, blank=True, null=True, verbose_name=_('Instagram'))

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Team'



class Hitofsales(models.Model):
    image = models.ImageField(upload_to='photos/about', blank=True, null=True, verbose_name=_('Image 1'))

    def __str__(self):
        return str(('image'))

    class Meta:
        verbose_name = _('Hit Of Sales')
        verbose_name_plural = _('Hit Of Sales')
from django.db import models
from ckeditor.fields import RichTextField
from parler.models import TranslatableModel, TranslatedFields
from django.utils.translation import gettext_lazy as _

class Bannerhome(TranslatableModel):
    image = models.ImageField(upload_to='photos/about', blank=True, null=True, verbose_name=_('Banner fottosi'))
    translations = TranslatedFields(
        title = models.CharField(max_length=250, verbose_name=_('Name')),
        text = RichTextField(verbose_name=_('Text')),
    )

    def save(self, *args, **kwargs):
        if not self.pk and Bannerhome.objects.exists():
            # Agar объект аллақачон бор бўлса, янги объект қўшилмайди
            raise Exception('Фақат битта баннер бўлиши мумкин!')
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.safe_translation_getter('title', any_language=True))
    class Meta:
        verbose_name = _('Banner ')
        verbose_name_plural = _('Banner')

class Bannerfoter(TranslatableModel):
    translations = TranslatedFields(
    title = models.CharField(max_length=250, verbose_name=_('Name')),
    text = RichTextField(verbose_name=_('Text')),
)