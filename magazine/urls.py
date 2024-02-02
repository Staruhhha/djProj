from django.urls import path
from .views import *

urlpatterns = [
    path ('index/', home, name='home_page'),
    path('catalog/', catalog_product, name='catalog_product_page'),
    path('product/<int:pk>/', product_detail, name='detail_product_page'),

    path('suppliers/', catalog_supplier, name='catalog_supplier_page'),
    path('supplier/<int:pk>', supplier_detail, name='detail_supplier_page'),
    path('supplier/create', supplier_create, name='create_supplier_page'),


    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name='log in'),
    path('logout/', user_logout, name='log out'),

    path('anon/', anon, name='anon'),
    path('auth/',auth, name='auth'),
    path('can_add/', can_add_product, name='can_add'),
    path('can_add_change/', can_add_and_change_product, name='can_add_change'),
    path('can_change_del/', change_delivery, name='can_change_del'),

    path('product/create', product_create, name='create_product_page')

]