"""
URL configuration for django_yfinance project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views  # Import views from the main project folder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('currency/', include('currency.urls')),  # If you have a currency app
    path('currency/<str:base>/<str:quote>/', include('currency.urls')),  # For the currency exchange rate
    #path('load_data/', include('load_data.urls')),  # If you have a load_data app
    path('', views.home, name='home'),  # Map the root URL to the home view
]