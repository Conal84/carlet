from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_all, name='all cars'),
]