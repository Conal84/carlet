from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_all, name='all_cars'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('car-insurance/<id>/', views.car_insurance, name='car_insurance'),
    path('car-insurance-skip/<car_id>/', views.car_insurance_skip, name='car_insurance_skip'),
    path('car-support/<id>/', views.car_support, name='car_support'),
    path('dashboard/', views.car_dashboard, name='car_dashboard'),
    path('add/', views.add_car, name='add_car'),
    path('display-cars/', views.display_cars, name='display_cars'),
    path('edit/<int:car_id>', views.edit_car, name='edit_car'),
    path('delete/<int:car_id>', views.delete_car, name='delete_car'),
    path('car-bookings/', views.car_bookings, name='car_bookings'),
]