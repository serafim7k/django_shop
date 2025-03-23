from django.shortcuts import render
from django.http import HttpResponse
from goods.models import Categories

def index(request):

    categories = Categories.objects.all()

    context = {
        'title': 'Home++',
        'content': 'Main shop page - Home++',
        'categories': categories,
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home++',
        'content': 'Main shop page - Home++',
        'some_text_about': 'About lorem ipsum dolor.',
    }
    return render(request, 'main/about.html', context)
