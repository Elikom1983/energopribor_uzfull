from django.shortcuts import render
from django.core.mail import send_mail
from energy.settings import DEFAULT_TO_EMAIL, EMAIL_HOST_USER
from .models import AboutImages, AboutMainImage, Partners, Team
from .forms import ContactForm
# Create your views here.
def about(request):
    about_image = AboutImages.objects.all()
    main_image = AboutMainImage.objects.all()
    context={
        'about_image':about_image,
        'main_image':main_image,
    }
    return render(request, 'pages/about.html', context)

def partners(request):
    partners = Partners.objects.all()
    context={
        'partners':partners,
    }
    return render(request, 'pages/partners.html', context)


def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            message = f"From: {name} \n email: {email} \n subject: {subject} \n message: {message}"

            send_mail('Contact', message, EMAIL_HOST_USER, [DEFAULT_TO_EMAIL])

            return render(request, "pages/contact.html", {'thanks': True})
    
        else:
            print(form.errors)
        
    return render(request, "pages/contact.html", {'form': form})

def team(request):
    team = Team.objects.all()
    context={
        'team':team,
    }
    return render(request, 'pages/team.html', context)
    