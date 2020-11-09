from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_all, name='all cars'),
    path('<car_id>', views.car_detail, name='car detail'),
    path('car-extra/', views.car_extra, name='car_extra'),
]