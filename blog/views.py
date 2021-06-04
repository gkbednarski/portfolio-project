from blog.models import Blog
from django.shortcuts import render, get_object_or_404
from django.http import request

def allblogs(request):
    blogs = Blog.objects
    return render(request, 'blogs/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detail.html', {'blog':detailblog})
