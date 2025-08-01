from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST #позволяет использовать функцию только с методом post
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                 override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request) #инициализируем корзину
    product = get_object_or_404(Product, id=product_id) #фильтруем все продукты оп id
    cart.remove(product)
    return redirect('cart:cart_detail')

#можно вставить декоратор только для зарегистрированных пользователей
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True,
        })
    return render(request, 'cart/cart_detail.html', {'cart': cart})
