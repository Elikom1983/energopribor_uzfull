
from django.shortcuts import render
from store.models import Product,Wishlist
from pages.models import Banner, Brand, Clients,Bannerhome,Bannerfoter,HomeSeo
from category.models import Category



def error_404(request, exception):
    return render(request, 'errors/404.html')

def error_500(request):
    return render(request, 'errors/404.html', status=500)


def home(request):
   # Охирги яратилган 10 та категорияни олиш
    categories = Category.objects.all().order_by('-id')[:10]

    top_products = Product.objects.all().order_by('-id')[:10]
    new_products = Product.objects.all().order_by('-created_date')[:10]
    banner = Banner.objects.all()
    brands = Brand.objects.all()
    clients = Clients.objects.all()
    populars = Category.objects.filter(is_popular=True)[:4]
    bannerhome = Bannerhome.objects.first()
    bannerfoter=Bannerfoter.objects.first()
    homeseo = HomeSeo.objects.first()


    context = { 
         'categories':categories,       
         'banner':banner,
         'top':top_products,
         'populars':populars,
         'bannerhome' : bannerhome,   
        'new':new_products,       
        'brands':brands,
        'clients':clients,
        'bannerfoter':bannerfoter,
        'homeseo':homeseo
    }
    return render(request, 'home.html', context)

def error_404(request, exception):
    return render(request, 'errors/404.html', status=404)

def error_500(request):
    return render(request, 'errors/404.html', status=500)
