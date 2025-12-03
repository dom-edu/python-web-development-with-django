from django.shortcuts import render
# from django.http import HttpResponse

from django.shortcuts import render


# each function is a view. 

def home(request):
    context = {
        'page_title': 'Home',
        'intro': 'Welcome to my portfolio! Here are some selected projects.',
        'name': 'Dom',
        'interests': ['computers','films']
    }
    return render(request, 'homepage/home.html', context)


def about(request):
    context = {
        'page_title': 'About',
        'bio': 'I am a developer who loves Python and web development.'
    }
    return render(request, 'homepage/about.html', context)


def projects(request):
    projects_data = [
        {'name': 'Weather App', 'tech': 'Django, API', 'desc': 'A small weather dashboard.'},
        {'name': 'Task Manager', 'tech': 'Django, JS', 'desc': 'A to-do CRUD app.'},
        {'name': 'Portfolio', 'tech': 'HTML, Django', 'desc': 'A personal site.'},
    ]
    context = {
        'page_title': 'Projects',
        'projects': projects_data
    }
    return render(request, 'homepage/projects.html', context)