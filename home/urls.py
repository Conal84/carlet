from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('how/', views.how_it_works, name='how_it_works'),
]