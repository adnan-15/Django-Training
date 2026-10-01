from django.shortcuts import render
from django.http import HttpResponse
from django.template import  loader
# Create your views here.
def testpaper(request):
    que="who developed python?"
    a="Ruchi jain"
    b="Vasima Khan"
    c="Guido van Rossum"
    d="Adnan khan"

    context={
        'que':que,
        'a':a,
        'b':b,
        'c':c,
        'd':d
    }

    template=loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)

def info(request):
    name="Iram khan"
    dept="Artificial intelligence"
    age="20"

    context={
        'name':name,
        'depta':dept,
        'age':age,
    }

    template=loader.get_template('info.html')
    res=template.render(context,request)
    return HttpResponse(res)
    
def add(request):
    total=10+20+30

    context={
        'a':10,
        'b':20,
        'c':30,
        'total':total,
    }

    template=loader.get_template('add.html')
    res=template.render(context,request)
    return HttpResponse(res)    

def result(request):
    context={
        'name': 'iram',
        'marks': 90,
    }

    return render(request, 'result.html', context)

def vote(result):
    context={
        'name': 'iram',
        'country': 'India',
        'age': 20,
    }

    return render(result, 'vote.html', context)

def home(request):
    return render(request, 'home.html', )

def about(request):
    return render(request, 'about.html', )

def contact(request):
    return render(request, 'contact.html', )