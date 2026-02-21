from django.shortcuts import render

# Functions for each HTML template
def page_404(request):
    return render(request, 'shared/404.html')

def about_us(request):
    return render(request, 'shared/about-us.html')

def contact(request):
    return render(request, 'shared/contact.html')

def home(request):
    return render(request, 'shared/home.html')

def index_2(request):
    return render(request, 'index-2.html')