from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('product/<int:id>/', views.product_detail, name='product-detail'),
    path('products/', views.product_list, name='list'),
    path('wishlist/', views.wishlist, name='wishlist'),
    ]


