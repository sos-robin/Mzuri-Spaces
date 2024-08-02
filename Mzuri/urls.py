# learningspaces/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('about/', About, name = "about"),
    path('contact/', Contact, name = "contact"),
    path('service/', Services, name = "services"),
    path('work/', Portfolio, name = "work"),

]
