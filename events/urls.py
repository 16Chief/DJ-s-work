from django.urls import path
from .views import event_list

urlpatterns = [
    path('', event_list, name='event_list'),
    # Add other event-related URLs here
]
