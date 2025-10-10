from category.models import Category
from site_settings.models import Footeraddres,Socials,PaymentMethod
from django.utils.translation import gettext_lazy as _
from django.urls import resolve
from store.models import Product, Wishlist

def site_settings(request):
    from .models import SiteSettings  # import ичида қўйиш
    settings = SiteSettings.objects.first()
    return {'site_settings': settings}



def latest_categories(request):
    categories = Category.objects.all().order_by('-id')[:10]  # охирги 10 та
    return {
        'latest_categories': categories
    }

def footeraddres(request):
    return {
        'footeraddres': Footeraddres.objects.first()
    }
def socials(request):
    return {
        'socials':Socials.objects.all()
    }
def paymentmethod(request):
    return{
        'paymentmethod':PaymentMethod.objects.all()
    }

def footercategory(request):
    categories = Category.objects.all()[:5]  # Фақат 5 та
    return {
        'footecategory': categories
    }
def menuall(request):
    categories = Category.objects.all().order_by('-id')  # охирги 10 та
    return {
        'menus': categories
    }


from category.models import Category
from store.models import Product

def breadcrumbs(request):
    path = request.path.strip('/').split('/')
    crumbs = []
    url = ''
    for slug in path:
        if not slug:
            continue
        url += '/' + slug
        name = None

        # Faqat category ва product учун чиқарамиз
        try:
            cat = Category.objects.get(slug=slug)
            name = cat.name
        except Category.DoesNotExist:
            pass

        try:
            prod = Product.objects.get(slug=slug)
            name = prod.safe_translation_getter("product_name", any_language=True)
        except Product.DoesNotExist:
            pass

        if name:  # Фақат топилган (category/product) чиқади
            crumbs.append({'name': name, 'url': url})
    
    return {'breadcrumbs': crumbs}
def wishlist_count(request):
    count = 0
    if request.user.is_authenticated:
        count = Wishlist.objects.filter(user=request.user).count()
    return {'wishlist_count': count}
