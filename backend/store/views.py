from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.core.paginator import Paginator

from .models import Product, Order, OrderItem
from category.models import Category, MetaDetail
from carts.models import Cart, CartItem
from .forms import OrderForm
from django.contrib.auth.decorators import login_required


# Session orqali cart_id olish
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# Do'kon sahifasi (kategoriya bo'yicha yoki umumiy)
def store(request, category_slug=None):
    products = None
    met = None   # har doim mavjud bo‘lsin

    if category_slug is not None:
        met = MetaDetail.objects.filter(category__slug=category_slug)
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category_id__in=[item.id for item in category.get_descendants(include_self=True)],
            is_available=True
        ).order_by('-created_date')
    else:
        products = Product.objects.filter(is_available=True).order_by('-created_date')

    paginator = Paginator(products, 15)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        'products': products,
        'page': page,
        'met': met,
    }
    return render(request, 'store/store.html', context)


# Maxsulot batafsil sahifasi
def product_detail(request, category_slug, product_slug):
    single_product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    new_products = Product.objects.order_by('-created_date')[:10]

    context = {
        'single_product': single_product,
        'new': new_products,
    }
    return render(request, 'store/product_detail.html', context)


# Kategoriya ro'yxati
def store_category(request):
    categories = Category.objects.all().order_by('name')

    paginator = Paginator(categories, 15)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    context = {
        'category': categories,
        'page': page,
    }
    return render(request, 'store/category.html', context)


# Buyurtma qilish (checkout)
def checkout(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = Order(**form.cleaned_data)
            order.save()

            cart = Cart.objects.filter(cart_id=_cart_id(request), is_active=True).first()
            if cart:
                cart_items = CartItem.objects.filter(cart=cart, is_active=True)
                for cart_item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        product=cart_item.product,
                        quantity=cart_item.quantity
                    )
                cart_items.update(is_active=False)
                cart.is_active = False
                cart.save()

            return redirect('complete')

    else:
        form = OrderForm()

    return render(request, 'store/checkout.html', {'form': form})


# Buyurtma tugaganidan keyin
def complete(request):
    return render(request, 'store/thanks.html')


# Qidiruv
def search(request):
    product_search = []
    product_count = 0

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            product_search = Product.objects.order_by('-created_date').filter(
                Q(translations__description__icontains=keyword) |
                Q(translations__product_name__icontains=keyword)
            )
            product_count = product_search.count()

    context = {
        'product_search': product_search,
        'product_count': product_count,
    }
    return render(request, 'store/search.html', context)
login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'items': items})


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.filter(user=request.user, product=product).delete()
    return redirect('wishlist')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    # TODO: cart logikani yozish
    return redirect('cart_detail')

def remove_from_cart(request, product_id):
    # TODO: mahsulotni cartdan o‘chirish
    return redirect('cart_detail')

def cart_detail(request):
    # TODO: cartni ko‘rsatish
    return render(request, 'store/cart.html')