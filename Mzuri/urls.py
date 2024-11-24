# learningspaces/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', About, name = "about"),
    path('contact/', Contact_view, name = "contact"),
    path('service/', Services, name = "services"),
    path('work/', Portfolio, name = "work"),
    path('products/', Product, name = "product"),
    path('thank-you/',Thank_you_view, name='thank_you'),

]
