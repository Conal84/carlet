from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_all, name='all cars'),
    path('<car_id>', views.car_detail, name='car detail'),
    path('extras/', views.car_extras, name='car extras'),
]