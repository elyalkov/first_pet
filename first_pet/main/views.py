from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.contrib.auth.forms import UserCreationForm


def product_list(request, category_slug=None): #ategory_slug - параметр запроса при фильтрации
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'main/product_list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    #return render(request,
                  #'main/detail.html',
                  #{'product': product})

    return render(request,
                  'main/detail.html',
                  {'product': product,
                            'cart_product_form': cart_product_form})


def register(request):
        if request.method == 'POST': #проверяем, нажал ли пользователь на конпку "Зарегистрировться"
            form = UserCreationForm(request.POST) #выдаем форму регистрации пользователя от Django
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()

        return render(request, 'registration/register.html', {'form': form})