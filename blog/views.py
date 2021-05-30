from blog.models import Blog
from django.shortcuts import render
from django.http import request

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blogs/allblogs.html', {'blogs':blogs})
