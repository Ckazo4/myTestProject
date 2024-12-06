from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home',
        'content': 'Добро пожаловать на сайт Суши Осака'
    }

    return render(request, 'main/index.html', context)

def about(request):
    return render('About page')