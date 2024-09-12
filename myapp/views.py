from django.shortcuts import render
from myapp.models import Post
# Create your views here.

def post_list(request):
    post_lists = Post.objects.all()
    context = {
        "post_list": post_lists,
    }
    return render(
        request,
        "post_list.html",
        context=context,
    )

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
        'publisher_recently': post.publisher_recently(),
    }
    return render(
        request,
        "post_detail.html",
        context=context,
    )