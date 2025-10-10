from django.urls import path
from . import views
urlpatterns = [
    path('', views.oferta, name='oferta'),  # /oferta/
]
# backend/oferta/urls.py