from django.shortcuts import render

def index(request):

    context = {
        'name': 'Jaime Andrade',
        'projects': [],
        'blogs': [],
        'contact': '0992814433'
    }
    return render(request, 'home/index.html', context)

def project(request, pk):
    return render(request, 'home/project.html')

def blog(request, pk):
    return render(request, 'home/detail_blog.html')
