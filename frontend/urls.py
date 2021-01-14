
from django.contrib import admin
from django.urls import path 
from . import views

urlpatterns = [
    path('', views.MainView.as_view() ,name='home'),
    # path('footer', views.footer),
]
