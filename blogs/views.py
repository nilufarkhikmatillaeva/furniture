from django.shortcuts import render

def blog_detail(request):
    return render(request, 'blogs/blog-detail.html')

def blog_list(request):
    return render(request, 'blogs/blog-list.html')