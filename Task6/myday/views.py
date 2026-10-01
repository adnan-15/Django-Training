from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from myday.models import Product
from django.urls import reverse

def newproduct(request):
    res=render(request,'newproduct.html')
    return res
# Create your views here.
def createproduct(request):
    p_id = request.POST['p_id']
    p_name = request.POST['p_name']
    p_price = request.POST['p_price']
    p_offer = request.POST['p_offer']
    P = Product(p_id=p_id, p_name=p_name, p_price=p_price, p_offer=p_offer)
    P.save()
    url = reverse('productlist')
    return HttpResponseRedirect(url)

def plist(request):
    plistt = Product.objects.all()
    res=render(request,'productlist.html',{'plist':plistt})
    return res

def updateProductlist(request):
    id = request.GET['id']
    product = Product.objects.filter(id=id).values()
    res=render(request,'updatedProductlist.html',{'product':product[0]})
    return res

def updateProduct(request):                #update record , u of crud
    id=request.POST['id']
    p_id = request.POST['p_id']
    p_name = request.POST['p_name']
    p_price = request.POST['p_price']
    p_offer = request.POST['p_offer']
    Product(p_id=p_id, p_name=p_name, p_price=p_price, p_offer=p_offer).save()
    url=reverse('productlist')
    return HttpResponseRedirect(url)

def deleteProduct(request):
    id=request.GET['id']
    pro=Product.objects.filter(id=id)
    pro.delete()
    url=reverse('productlist')
    return HttpResponseRedirect(url)