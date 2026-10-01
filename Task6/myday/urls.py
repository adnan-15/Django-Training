from django.urls import path 
from . views import *

urlpatterns=[
    path('deleteProduct/',deleteProduct,name='deleteProduct'),
    path('updateProduct/',updateProduct,name='updateProduct'),
    path('productlist/',plist, name='productlist'),
    path('createproduct/',createproduct,name='createproduct'),
    path('newproduct/',newproduct,name='newproduct'),
    path('updateProductlist/',updateProductlist,name='updateProductlist'),
]