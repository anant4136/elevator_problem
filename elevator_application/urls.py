from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('elevator', ElevatorView.as_view(), name='Elevator'),
]
