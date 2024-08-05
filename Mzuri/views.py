from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'Mzuri/index.html')

def About(request):
    
    return render(request,'Mzuri/about.html')


def Contact(request):
    
    return render(request,'Mzuri/contact.html')

def Services(request):
    
    return render(request,'Mzuri/services.html')

def Portfolio(request):
    
    return render(request,'Mzuri/work.html')

def Product(request):
    
    return render(request,'Mzuri/shop.html')