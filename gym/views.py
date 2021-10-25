from django.shortcuts import render

# Create your views here.

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Login(request):
    return render(request, 'login.html')
