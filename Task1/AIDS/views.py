from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def About_AIDS(request):
    s="<h4>This is AIDS page</h4> <br> <h1>The B.Tech in Computer Science and Engineering (CSE) with Artificial Intelligence and Data Science (AIDS) at Sagar Institute of Science and Technology (SISTec) in Bhopal is a four-year undergraduate engineering program designed to train students for futuristic, tech-driven industries</h1>"
    return HttpResponse(s)