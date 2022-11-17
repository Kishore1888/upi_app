from django.urls import path
from .import views

urlpatterns=[
    # form is the view function name
    path('loginpage',views.forms), 
    path('homepage',views.homepage), 
    path('home',views.home),
    path("qrcode",views.qrcode_page)
] 