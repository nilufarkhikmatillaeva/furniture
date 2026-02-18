from django.urls import path
from . import views

urlpatterns = [
    path('404/', views.page_404, name='404'),
    path('about-us/', views.about_us, name='about-us'),
    path('account/', views.account, name='account'),
    path('blog/<int:id>/', views.blog_detail, name='blog-detail'),
    path('blog/', views.blog_list, name='blog-list'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),  # home page
    path('index-2/', views.index_2, name='index-2'),
    path('login/', views.login, name='login'),
    path('product/<int:id>/', views.product_detail, name='product-detail'),
    path('products/', views.product_list, name='product-list'),
    path('register/', views.register, name='register'),
    path('reset-password/', views.reset_password, name='reset-password'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
