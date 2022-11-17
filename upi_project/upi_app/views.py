from django.http import HttpResponse
from django.shortcuts import render

from .forms import application_form

# Create your views here.
def forms(request):
    form=application_form
    if request.method=="POST":
        form=application_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("success")
    return render(request,"login_page.html",{'form':form})
    
def homepage(request):
    return render(request,"home_page.html")

def home(request):
    return render(request,"home.html")

def qrcode_page(request):
    return render(request,"qr_code_page.html")