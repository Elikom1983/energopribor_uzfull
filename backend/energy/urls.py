from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),
    path('pages/', include('pages.urls')),
    path('news/', include('news.urls')),
    path('about/', include('about.urls')),
    path('contacts/', include('conatact.urls')),
    path('faq/', include('faq.urls')),
    path('vacansiya/', include('vacansiya.urls')),
    path('oferta/', include('oferta.urls')),
      

    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    ),
    path(
        "sitemap.xml",
        TemplateView.as_view(template_name="sitemap.xml", content_type="text/xml"),
    ),
)

urlpatterns += [
    re_path(r'^rosetta/', include('rosetta.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

handler500 = 'energy.views.error_500'
handler404 = 'energy.views.error_404'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
