from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Product
from .models import Cart, Cart_item


# Create your views here.
# Creating Sessiom

def my_cart(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


# add product to cart
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    try:
        cart = Cart.objects.get(cart_id=my_cart(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=my_cart(request))
        cart.save()

    try:
        cart_item = Cart_item.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
            cart_item.save()
    except Cart_item.DoesNotExist:
        cart_item = Cart_item.objects.create(product=product, cart=cart, quantity=1)
        cart_item.save()
    return redirect('cart:cartdetails')


# cart details
def cart_details(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=my_cart(request))
        cart_items = Cart_item.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


# delete product
def remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=my_cart(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart_item.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cartdetails')


# reduce product quantity
def reduce_quantity(request, product_id):
    cart = Cart.objects.get(cart_id=my_cart(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = Cart_item.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cartdetails')
