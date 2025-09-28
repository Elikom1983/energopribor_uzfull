from category.models import Category
from site_settings.models import Footeraddres,Socials,PaymentMethod

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
