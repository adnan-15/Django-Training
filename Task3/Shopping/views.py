from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def shop(result):
    return render(result, 'shopping.html', )