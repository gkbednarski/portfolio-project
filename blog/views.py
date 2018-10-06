from django.shortcuts import render, get_object_or_404
from .models import Blog

def allblogs(request):
  blogView=Blog.objects
  return render(request, 'blog/allblogs.html',{'blogView':blogView})

def detail(request, blog_id):
  detailblock=get_object_or_404(Blog, pk=blog_id)
  return render(request,'blog/detail.html',{'blog':detailblock})
