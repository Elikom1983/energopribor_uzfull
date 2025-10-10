from django.shortcuts import render
from conatact.models import Contact

def contact(request):
    contact = Contact.objects.first()   
    context = {
        'contact': contact
    }
    return render(request, "pages/contact.html", context)

