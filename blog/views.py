from django.shortcuts import render
from mainPage.models import Post, PostDescription, PostImgUrl
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog(request):
    posts = Post.objects.values('post_id', 'author', 'postimgurl__img_url',
                                'postdescription__description', 'created', 'title')

    paginator = Paginator(posts, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/blog-content.html', context={
        'posts': posts,
        'page': page
    })


def single_blog(request):
    return render(request, 'blog/blog-single.html')
