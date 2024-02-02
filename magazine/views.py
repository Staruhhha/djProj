from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    return render(request, 'index.html')

# Create your views here.

def catalog_product(request):
    product_list = Product.objects.filter(exists=True).order_by('-name')
    context = {
        'list_object': product_list
    }
    return render(request, 'product/catalog.html', context)


def product_detail(request, pk):
    if request.method == "POST":
        messages.success(request,"Добавлен в корзину")
        return redirect('catalog_product_page')
    else:
        product = get_object_or_404(Product, pk=pk)
        context = {
            'product': product
        }
    return render(request, 'product/detail.html', context)


@permission_required('magazine.view_supplier')
def catalog_supplier(request):
    supplier_list = Supplier.objects.order_by('-name')
    context = {
        'list_sup': supplier_list
    }
    return render(request, 'supplier/catalog.html', context)

@permission_required('magazine.view_supplier')
def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    context = {
        'supplier': supplier
    }
    return render(request, 'supplier/detail.html', context)


@permission_required('magazine.add_supplier')
def supplier_create(request):
    if request.method == "POST":
        form_supplier = SupplierForm(request.POST)
        if form_supplier.is_valid():
            form_supplier.save()
            messages.success(request, 'Поставщик успешно добавлен')
            return redirect('catalog_suppliers_page')

        messages.error(request, 'Неверно заполнены поля')

    else:
        form_supplier = SupplierForm()

        context = {
            'form': form_supplier
        }
        return render(request, 'supplier/create.html', context)



@permission_required('magazine.add_product')
def product_create(request):
    if request.method == "POST":
        form_product = ProductForm(request.POST)
        if form_product.is_valid():
            form_product.save()
            messages.success(request, 'Продукт успешно добавлен')
            return redirect('catalog_product_page')
        messages.error(request, 'неправильно заполнены поля')
    else:
        form_product = ProductForm()
    context = {
        'form': form_product
    }
    return render(request, 'product/create.html', context)




#------------------------авторизация в приложении-------------------------

def user_registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            print(user)

            login(request, user)

            messages.success(request, 'успешная регистрация')
            return redirect('home_page')

        messages.error(request, "Произошла проблема")

    else:
        form = RegistrationForm()
    return render(request, 'auth/registration.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()

            print('is_anon:', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)

            login(request, user)

            print('is_anon:', request.user.is_anonymous)
            print('is_auth', request.user.is_authenticated)
            print(user)

            messages.success(request, 'Вы успешно авторизовались')
            return redirect('home_page')

        messages.error(request, "ой, ошибка")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.warning(request, 'вы вышли из аккаунта')
    return redirect('log in')


def anon(request):
    print('is_active:', request.user.is_active)
    print('is_anonymous:',request.user.is_anonymous)
    print('is_authenticated:',request.user.is_authenticated)
    print('is_staff:', request.user.is_staff)
    print('is_superuser:', request.user.is_superuser)

    print('может добавлять товар?',request.user.has_perm('magazine.add_product'))
    print('может добавлять или изменять товар', request.user.has_perms(['magazine.add_product', 'magazine.change_product']))
    print('может менять способ доставки', request.user.has_perm('magazine.change_delivery_type'))

    return render(request, 'test/anon.html')


@login_required()
def auth(request):
    return render(request, 'test/auth.html')


@permission_required('magazine.add_product')
def can_add_product(request):
    return render(request, 'test/can_add_product.html')


@permission_required(['magazine.add_product', 'magazine.change_prodcut'])
def can_add_and_change_product(request):
    return render(request, 'test/can_change_and_add_product.html')

@permission_required('magazine.change_delivery_type')
def change_delivery(request):
    return render(request, 'test/change_delivery_type.html')


