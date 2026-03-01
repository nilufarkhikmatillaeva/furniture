from django.urls import path
from . import views

app_name = 'shared'

urlpatterns = [
    path('404/', views.page_404, name='404'),
    path('about-us/', views.about_us, name="about"),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
]