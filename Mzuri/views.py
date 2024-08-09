from django.shortcuts import render
from .models import Buy_product

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages



def home(request):
    
    return render(request, 'Mzuri/index.html')

def About(request):
    
    return render(request,'Mzuri/about.html')


#def Contact(request):
    
    return render(request,'Mzuri/contact.html')

def Services(request):
    
    return render(request,'Mzuri/services.html')

def Portfolio(request):
    
    return render(request,'Mzuri/work.html')

def Product(request):
    products = Buy_product.objects.all()
    return render(request, 'Mzuri/shop.html', {'products': products})

def Contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('thank_you')
    else:
        form = ContactForm()

    return render(request, 'Mzuri/contact.html', {'form': form})

def Thank_you_view(request):
    return render(request, 'Mzuri/thank_you.html')