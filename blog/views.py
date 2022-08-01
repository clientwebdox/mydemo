from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from blog.models import Post
from blog.forms import PostForm

def home(request):
    posts= Post.objects.all()
    context={'posts':posts}
    return render(request, "blog/index.html", context)
def about(request):
    return render(request, "blog/about.html")
def contact(request):
    return render(request, "blog/contact.html")
def post(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post.html", {'post': post})
    # return HttpResonse(post)

def createpost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, "blog/post_create.html", {'form': form})




def editpost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_create.html", {'form': form})