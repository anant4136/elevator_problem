from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('elevator/create_elevators/',
         ElevatorView.as_view({'post': 'create_elevators'}), name='create_elevators'),
    path('elevator/process_requests/',
         ElevatorView.as_view({'post': 'process_requests'}), name='process_requests'),
    path('elevator/destination_requests/', ElevatorView.as_view(
        {'post': 'destination_requests'}), name='destination_requests'),
]
