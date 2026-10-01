from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Greeting(request):
    s="<h1>Iram Khan</h1>"
    return HttpResponse(s)

def College(request):
    s="<h1>SISTEC</h1>"
    return HttpResponse(s)

def Department(request):
    s="<h1>Artificial Intelligence and Data Science</h1>"
    return HttpResponse(s)