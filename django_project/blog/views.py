from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def projects(request):
    return render(request, 'blog/projects.html')

def contact(request):
    return render(request, 'blog/contact.html')



posts = [
    {
        "author": "charles carden",
        "title": "blog post 1",
        "description": "First content",
        "date_posted": "august 2020"
    },
    {
        "author": "bio",
        "title": "blog post 2",
        "description": "second content",
        "date_posted": "august 3, 2020"
    }
]