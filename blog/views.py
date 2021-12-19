from django.shortcuts import render, get_object_or_404
from mainPage.models import Post, PostDescription, PostImgUrl
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog(request):
    posts = Post.objects.all()

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


def single_blog(request, post, pk):
    post = get_object_or_404(Post, slug=post, pk=pk)
    return render(request, 'blog/blog-single.html', {'posts': post})
