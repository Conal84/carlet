from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_all, name='all cars'),
    path('<car_id>', views.car_detail, name='car detail'),
    path('car-insurance/', views.car_insurance, name='car_insurance'),
    path('car-support/', views.car_support, name='car_support'),
]