from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Home',
        'content': 'Main shop page - Home',
        'list': ['first', 1],
        'dict': {'second': 2},
        'is_aunthenticated': True,
    }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('Hello ABOUT page')
