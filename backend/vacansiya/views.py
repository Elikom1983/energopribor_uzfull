from django.shortcuts import render
from vacansiya.models import *

def vacansiya(request):
    vakansiya=Vacansiya.objects.first()
    vakansiyaitem=VacansiyaItem.objects.all()
    data={
        'vakansiya':vakansiya,
        'vakansiyaitem':vakansiyaitem

    } 
    return render(request, "pages/vacanisya.html", data)
