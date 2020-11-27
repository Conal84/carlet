from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_all, name='all_cars'),
    path('<car_id>', views.car_detail, name='car_detail'),
    path('car-insurance/', views.car_insurance, name='car_insurance'),
    path('car-insurance/<car_id>', views.car_insurance_skip, name='car_insurance_skip'),
    path('car-support/', views.car_support, name='car_support'),
    # path('car-support/<car_id>', views.car_support_skip, name='car_support_skip'),
]