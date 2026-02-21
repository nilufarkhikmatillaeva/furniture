from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('<int:id>/', views.blog_detail, name='detail'),
    path('', views.blog_list, name='list'),
]