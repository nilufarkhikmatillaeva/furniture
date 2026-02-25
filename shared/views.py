from django.shortcuts import render

from .models import Staff


def page_404(request):
    return render(request, 'shared/404.html')

def about_us(request):
    context = {
        'staff' : Staff.objects.all(),
    }
    return render(
        request, 'shared/about-us.html',
        context
    )
def contact(request):
    return render(request, 'shared/contact.html')

def home(request):
    return render(request, 'shared/home.html')

def index_2(request):
    return render(request, 'index-2.html')