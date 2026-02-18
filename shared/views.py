from django.shortcuts import render

# Functions for each HTML template
def page_404(request):
    return render(request, 'shared/404.html')

def about_us(request):
    return render(request, 'shared/about-us.html')

def account(request):
    return render(request, 'users/account.html')

def blog_detail(request):
    return render(request, 'blogs/blog-detail.html')

def blog_list(request):
    return render(request, 'blogs/blog-list.html')

def cart(request):
    return render(request, 'products/cart.html')

def checkout(request):
    return render(request, 'products/checkout.html')

def contact(request):
    return render(request, 'shared/contact.html')

def home(request):
    return render(request, 'shared/home.html')

def index_2(request):
    return render(request, 'index-2.html')

def login(request):
    return render(request, 'users/login.html')

def product_detail(request):
    return render(request, 'products/product-detail.html')

def product_list(request):
    return render(request, 'products/product-list.html')

def register(request):
    return render(request, 'users/register.html')

def reset_password(request):
    return render(request, 'users/reset-password.html')

def wishlist(request):
    return render(request, 'products/wishlist.html')
