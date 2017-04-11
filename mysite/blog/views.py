from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

def index(request):
    return render(request, 'header.html')
