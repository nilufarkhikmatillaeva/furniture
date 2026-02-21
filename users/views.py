from django.shortcuts import render

def register(request):
    return render(request, 'users/register.html')

def reset_password(request):
    return render(request, 'users/reset-password.html')

def account(request):
    return render(request, 'users/account.html')

def login(request):
    return render(request, 'users/login.html')