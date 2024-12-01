from django.urls import path
from . import views

#app_name = 'currency'

urlpatterns = [
    #path('get_currencies/', views.get_currencies, name='get_currencies'),
    
    path('', views.get_currencies, name='get_currencies'),
    path('<str:base>/<str:quote>/', views.get_exchange_rate, name='get_exchange_rate'),
    path('load_data/', views.load_data, name='load_data'),
]