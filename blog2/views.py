from django.shortcuts import render

# Create your views here.
from blog2.models import Page


def about2(request):
    posts = Page.objects.get(pk=1)
    context = {'posts': posts}
    return render(request, "blog2/about2.html",context)