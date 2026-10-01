from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    s="<h4>This is Home page</h4> <br> <h1> Sagar Institute of Science and Technology (SISTec) is a private technical education group in Bhopal, Madhya Pradesh, established in 2007 under the Sagar Group of Institutions.</h1>"
    return HttpResponse(s)
