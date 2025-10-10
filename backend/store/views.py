from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import json

from .models import Product, Order, OrderItem
from category.models import Category, MetaDetail
from store.models import Wishlist,Attribute
from carts.models import Cart, CartItem
from .forms import OrderForm
from django.db.models import Min, Max

from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from dal import autocomplete
from .models import AttributeValue
from django.db.models import Q

# views.py бошига қўшинг
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


class AttributeValueAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = AttributeValue.objects.all()
        if self.q:
            qs = qs.filter(translations__value__icontains=self.q)
        return qs

    def has_add_permission(self, request):
        return True

    def create_object(self, text):
        obj = ProductAttributeValue()
        obj.set_current_language('uz')
        obj.value = text
        obj.save()
        return obj
# Do'kon sahifasi
def store(request, category_slug=None):
    products = Product.objects.filter(is_available=True).order_by('-created_date')
    category = None
    met = None

    # 🔹 Kategoriya bo‘yicha filter
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        met = MetaDetail.objects.filter(category__slug=category_slug)
        products = products.filter(
            category_id__in=[item.id for item in category.get_descendants(include_self=True)]
        )

    # 🔹 AJAX orqali filter so‘rovi bo‘lsa
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        price_min = request.GET.get('price_min')
        price_max = request.GET.get('price_max')
        discount = request.GET.get('discount')
        search = request.GET.get('search')

        # ✅ Narx oralig‘iga qarab filter
        if price_min and price_max:
            products = products.filter(price__gte=price_min, price__lte=price_max)

        # ✅ Chegirma bo‘yicha filter
        if discount:
            products = products.filter(discount__gte=int(discount))

        # ✅ Qidiruv (nom yoki tavsif bo‘yicha)
        if search:
            products = products.filter(
                Q(translations__product_name__icontains=search) |
                Q(translations__description__icontains=search)
            )

        paginator = Paginator(products, 15)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)

        # 🔹 AJAX javob sifatida faqat product listni qaytaramiz
        return render(request, 'store/partials/product_list.html', {'page': page})

    # 🔹 Oddiy (non-AJAX) sahifa
    paginator = Paginator(products, 15)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    attributes = Attribute.objects.all().prefetch_related('values')
    price_range = products.aggregate(min_price=Min('price'), max_price=Max('price') )

    context = {
        'products': products,
        'page': page,
        'met': met,
        'category': category,
        'product_count': products.count(),
        'attributes': attributes, 
        "price_range":price_range
    }
    return render(request, 'store/store.html', context)

# Mahsulot batafsil sahifasi
def product_detail(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
    new_products = Product.objects.order_by('-created_date')[:10]
    gallery_images = product.gallery.all()

    context = {
        'single_product': product,
        'related_products': related_products,
        'new': new_products,
        'gallery': gallery_images,
    }
    return render(request, 'store/single_page.html', context)


# Kategoriya ro'yxati
def store_category(request):
    categories = Category.objects.all().order_by('name')
    paginator = Paginator(categories, 15)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {'category': categories, 'page': page}
    return render(request, 'store/category.html', context)




def checkout(request):
    cart = Cart.objects.filter(cart_id=_cart_id(request), is_active=True).first()
    cart_items = CartItem.objects.filter(cart=cart, is_active=True)
    cart_total = sum(i.product.price * i.quantity for i in cart_items)

    if request.method == 'POST':
        first_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        delivery = request.POST.get('delivery_type')
        comment = request.POST.get('comment')
        payment = request.POST.get('payment_method')

        # agar foydalanuvchi chek yuklasa
        receipt = request.FILES.get('transfer_receipt')
        transfer_amount = request.POST.get('transfer_amount')

        order = Order.objects.create(
            first_name=first_name,
            phone=phone,
            address_line=address,
            delivery_type=delivery,
            comment=comment,
            payment_method=payment,
            total_price=cart_total,
            transfer_amount=transfer_amount or 0,
            transfer_receipt=receipt
        )

        for item in cart_items:
            OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

        cart_items.update(is_active=False)
        cart.is_active = False
        cart.save()

        return redirect('store:complete')

    context = {'cart_items': cart_items, 'cart_total': cart_total}
    return render(request, 'store/checkout.html', context)
# Buyurtma tugagandan keyin
def complete(request):
    return render(request, 'store/thanks.html')


# Qidiruv
def search(request):
    keyword = request.GET.get('keyword')
    products = Product.objects.none()
    product_count = 0
    if keyword:
        products = Product.objects.order_by('-created_date').filter(
            Q(translations__description__icontains=keyword) |
            Q(translations__product_name__icontains=keyword)
        )
        product_count = products.count()

    return render(request, 'store/search.html', {'product_search': products, 'product_count': product_count})


# Wishlist
@login_required
def wishlist(request):
    items = Wishlist.objects.filter(user=request.user)
    return render(request, 'store/wishlist.html', {'items': items})


@login_required
def toggle_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=request.user, product=product)
    if not created:
        wishlist_item.delete()
        return JsonResponse({'status': 'removed'})
    return JsonResponse({'status': 'added'})


@login_required
def clear_wishlist(request):
    if request.method == 'POST':
        Wishlist.objects.filter(user=request.user).delete()
        return JsonResponse({'status': 'cleared'})


# Cart funksiyalari
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Саватни олиш ёки яратиш
    cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request), is_active=True)

    # CartItem ни олиш ёки яратиш
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, is_active=True)

    # Агар олдиндан бўлса, quantity ошириш
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    # Namespace билан redirect
    return redirect('store:cart_detail')


@login_required
def remove_from_cart(request, product_id):
    cart = Cart.objects.filter(cart_id=_cart_id(request), is_active=True).first()
    if cart:
        item = CartItem.objects.filter(cart=cart, product_id=product_id, is_active=True).first()
        if item:
            item.delete()
    return redirect('cart_detail')


def cart_detail(request):
    cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request), is_active=True)
    items = CartItem.objects.filter(cart=cart, is_active=True)
    total = sum(i.product.price * i.quantity for i in items)
    return render(request, 'store/cart.html', {'cart_items': items, 'cart_total': total})


def update_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        quantity = data.get('quantity')
        try:
            item = CartItem.objects.get(id=item_id)
            item.quantity = quantity
            item.save()

            cart_items = CartItem.objects.filter(cart=item.cart, is_active=True)
            cart_total = sum(i.product.price * i.quantity for i in cart_items)
            cart_total_formatted = f"{cart_total:,}"

            return JsonResponse({'success': True, 'cart_total_formatted': cart_total_formatted})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})
# AJAX: remove cart item

def remove_cart_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('item_id')
        try:
            item = CartItem.objects.get(id=item_id)
            cart = item.cart
            item.delete()

            cart_items = CartItem.objects.filter(cart=cart, is_active=True)
            cart_empty = not cart_items.exists()
            cart_total = sum(i.product.price * i.quantity for i in cart_items)
            cart_total_formatted = f"{cart_total:,}"

            return JsonResponse({'success': True, 'cart_total_formatted': cart_total_formatted, 'cart_empty': cart_empty})
        except CartItem.DoesNotExist:
            return JsonResponse({'success': False})
    return JsonResponse({'success': False})


@csrf_exempt
def ajax_filter_products(request):
    import traceback
    from django.http import HttpResponse

    try:
        if request.method == "POST":
            data = json.loads(request.body)
            print("📦 Kelayotgan filterlar:", data)

            products = Product.objects.filter(is_available=True)

            # 🔹 Narx filteri
            min_price = data.get("min_price")
            max_price = data.get("max_price")
            if min_price and max_price:
                products = products.filter(price__gte=min_price, price__lte=max_price)

            # 🔹 Atributlar bo‘yicha filter
            for key, values in data.items():
                if key in ["min_price", "max_price", "sort"]:
                    continue
                if not values:
                    continue

                if not Attribute.objects.filter(slug=key).exists():
                    print(f"⚠️ Attribute topilmadi: {key}")
                    continue

                try:
                    products = products.filter(
                        attribute_values__attribute__slug=key,
                        attribute_values__value__in=values
                    ).distinct()
                    print(f"✅ Filter qo‘llandi: {key} = {values}")
                except Exception as e:
                    print(f"❌ Filter xatosi: {key} => {e}")

            # 🔹 Saralash
            sort = data.get("sort")
            if sort == "price_asc":
                products = products.order_by("price")
            elif sort == "price_desc":
                products = products.order_by("-price")
            elif sort == "name_asc":
                products = products.order_by("translations__product_name")

            # 🔹 HTML qaytarish
            html = render_to_string("store/partials/product_list.html", {"products": products})
            return JsonResponse({"html": html})

        return JsonResponse({"error": "Invalid method"})
    except Exception:
        traceback.print_exc()
        return HttpResponse(f"<pre>{traceback.format_exc()}</pre>", status=500)
    
