from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Q
from mainPage.models import Post, PostDescription, Comment
from .forms import CommentForm


def blog(request):
    posts = Post.objects.values('title', 'postdescription__description', 'author', 'created', 'comment_user',
                                'img_primary', 'comment', 'slug', 'post_id').annotate(
        commentcount=Count('comment_user'))
    all_post = Post.objects.order_by('-updated').all()[:5]

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
        'page': page,
        'all_post': all_post
    })


def single_blog(request, post, pk):
    all_post = Post.objects.order_by('-updated').all()[:5]
    post = get_object_or_404(Post, slug=post, pk=pk)
    post_desc = PostDescription.objects.filter(post=post)
    comment = Comment.objects.filter(post=post)
    new_comment = None
    if request.method == 'POST':
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            new_comment = form_comment.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
    else:
        form_comment = CommentForm()

    return render(request, 'blog/blog-single.html', {
        'posts': post,
        'desc': post_desc,
        'comments': comment,
        'form': form_comment,
        'new_comment': new_comment,
        'all_post': all_post
    })


class SearchList(ListView):
    paginate_by = 3
    template_name = 'blog/blog-search.html'
    context_object_name = 'all_search'

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Post.objects.filter(Q(postdescription__description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
