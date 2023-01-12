from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('doctors/', views.doctors, name='doctors'),
    path('reviews', views.reviews, name='reviews'),
    path('register/', views.register, name='register'),
    path('', views.index, name='home'),
]
