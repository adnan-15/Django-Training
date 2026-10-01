from django.urls import path
from App2 import views

urlpatterns=[
    path('Facebook/',views.Facebook),
    path('Linkedinn/',views.Linkedinn),
]