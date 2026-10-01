from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def About_CS(request):
    s="<h4>This is CS page</h4> <br> <h1>SISTec Computer Science & Engineering (CSE) is a 4-year undergraduate and 2-year postgraduate program offered by the Sagar Group of Institutions in Bhopal</h1>"
    return HttpResponse(s)

