from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def sistec(request):
    template=loader.get_template('sistec.html')
    return HttpResponse(template.render())