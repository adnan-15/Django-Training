from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Facebook(request):
    s="<h1>This is Facebook page </h1>"
    return HttpResponse(s)

def Linkedinn(request):
    s="<h1>This is Linkedinn page </h1>"
    return HttpResponse(s)