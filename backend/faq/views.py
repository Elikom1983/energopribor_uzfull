from django.shortcuts import render
from faq.models import Faq, FaqItem

def faq(request):
    faq = Faq.objects.first()  
    faq_items = FaqItem.objects.all()

    context = {
        "faq": faq,
        "faq_items": faq_items
    }
    return render(request, "pages/faq.html", context)
