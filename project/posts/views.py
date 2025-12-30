from django.http import HttpRequest
from django.shortcuts import render ,redirect , get_object_or_404
from .models import Post

# Create your views here.

def create_post(request:HttpRequest) -> HttpRequest:
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        author = request.user.username

        post = Post(title=title, content=content, author=author)
        post.save()



        return redirect(f'posts')

    if request.user.is_anonymous:
        return redirect('log_in')
    return render(request, 'posts/create_post.html')


def post(request:HttpRequest, post_id:int) -> HttpRequest:
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/post.html', {'post': post})


def posts(request: HttpRequest) -> HttpRequest:
    posts = Post.objects.all().order_by('-created_at')

    newest_post = posts.first() if posts.exists() else None
    other_posts = posts[1:] if posts.exists() else []

    return render(request, 'posts/posts.html', {
        'newest_post': newest_post,
        'other_posts': other_posts
    })
