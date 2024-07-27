# blog/views.py

from django.shortcuts import render
#from .models import Post

def home(request):
    return render(request, 'home.html')

# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/post_detail.html', {'post': post})


# main/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def handler404(request, exception):
    return render(request, 'blog/404.html', status=404)