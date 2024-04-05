from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('acerca-de-mi/', views.acerca_de_mi, name='acerca_de_mi'),
    path('contactame/', views.contactame, name='contactame'),
    path('mi-servicios/', views.servicios, name='servicios'),
]
