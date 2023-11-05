from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def demo(request):
    return render(request,"home.html")
def login(request):
    return render(request,"login.html")
def register(request):
    return render(request,"register.html")
def new_page(request):
    return render(request, 'new_page.html')

