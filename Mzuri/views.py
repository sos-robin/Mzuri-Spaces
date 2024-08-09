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
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Example: print form data or save to the database
            print(f"Name: {name}, Email: {email}, Subject: {subject}, Message: {message}")

            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Redirect to the same contact page or a thank you page
    else:
        form = ContactForm()

    return render(request, 'Mzuri/contact.html', {'form': form})