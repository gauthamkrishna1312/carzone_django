from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="HomePage"),
    path('about', views.about, name='about'),
    path('servies', views.servies, name='servies'),
    path('contact', views.contact, name='contact'),
]

