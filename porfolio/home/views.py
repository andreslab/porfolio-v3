from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):

    form = MessageForm()
    projects = Project.object.all()
    blogs = Blog.object.all()
    contact = Contact.object.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        return('/')

    context = {
        'name': 'Jaime Andrade',
        'projects': projects,
        'blogs': blogs,
        'contact': contact,
        'form': form
    }
    return render(request, 'home/index.html', context)

def project(request, pk):

    context = {
        'data': ''
    }

    return render(request, 'home/project.html', context)

def blog(request, pk):

    context = {
            'data': ''
        }

    return render(request, 'home/detail_blog.html', context)
