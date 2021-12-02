from django.shortcuts import render


def blog(request):
    return render(request, 'blog/blog-content.html')


def single_blog(request):
    return render(request, 'blog/blog-single.html')
