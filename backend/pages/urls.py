from . import  views
from django.urls import path
from django.conf.urls import handler404, handler500


urlpatterns = [
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
]