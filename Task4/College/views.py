from django.shortcuts import render
from django.http import HttpResponse
from django.template import  loader
# Create your views here.
def main(request):
    return render(request, 'main.html', )

def lnct(request):
    return render(request, 'lnct.html', )

def oict(request):
    return render(request, 'oict.html', )

def sistec(request):
    return render(request, 'sistec.html', )
