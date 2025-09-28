from .models import Category
from store.models import MetaWords
from pages.models import Hitofsales

def menu_links(request):
    categories = Category.objects.all()
    return {"cot": categories}


def meta_word(request):
    meta = MetaWords.objects.all()
    return {'meta': meta}

def hit_sale(request):
    hit = Hitofsales.objects.all()
    return {'hit': hit}