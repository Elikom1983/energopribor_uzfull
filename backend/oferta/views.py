from django.shortcuts import render
from .models import Oferta

def oferta(request):
    # Hozirgi tilga mos tarjimalarni olish
    oferta = Oferta.objects.first()  # Faqat bitta oferta obyekti deb hisoblaymiz

    context = {
        'oferta': oferta
    }
    return render(request, 'pages/oferta.html', context)
