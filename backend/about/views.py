from django.shortcuts import render
from about.models import *
from pages.models import Bannerhome

def about(request): 
    about=About.objects.first()
    number=Aboutnumber.objects.all()
    team=Team.objects.all()
    yutuq=Yutuqlar.objects.all()
    bannerhome = Bannerhome.objects.first()
    data={
        'about':about,
        'number':number,
        'team':team,
        'yutuq':yutuq,
        'bannerhome':bannerhome
    }   
    return render(request, "pages/about.html", data)
