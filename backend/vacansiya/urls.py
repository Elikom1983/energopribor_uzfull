from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacansiya, name='vakansiya')
    ]              
