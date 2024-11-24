from django.shortcuts import render
from .models import *

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404




def home(request):
    
    return render(request, 'Mzuri/index.html')

def About(request):
    
    return render(request,'Mzuri/about.html')


def Contact(request):
    
    return render(request,'Mzuri/contact.html')

def Services(request):
    
    return render(request,'Mzuri/services.html')

def Portfolio(request):
    # Fetch all portfolios
    portfolios = PortfolioSection.objects.all()
    
    # Pass the portfolios to the template
    return render(request, 'Mzuri/work.html', {'portfolios': portfolios})

def PortfolioPage(request, portfolio_id):
    # Retrieve the PortfolioSection object using portfolio_id
    portfolio = get_object_or_404(PortfolioSection, id=portfolio_id)
    
    # Retrieve all pictures related to the portfolio
    pictures = portfolio.company_pictures.all()

    return render(request, 'Mzuri/portfoliopage.html', {'portfolio': portfolio, 'pictures': pictures})

def Product(request):
    # Fetch all products and their related images
    products = BuyProduct.objects.prefetch_related('images').all()

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