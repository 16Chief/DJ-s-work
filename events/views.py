# views.py
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Event
from django.urls import reverse


def delete_event(request, event_id):
    if request.method == 'POST':
        event = Event.objects.get(id=event_id)
        event.delete()
        return redirect(reverse('category_list'))


def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('event_name')
        category_id = request.POST.get('event')
        start_date = request.POST.get('start_date')
        # Add your logic to create the event here
        # ...
        return redirect(reverse('category_list'))


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})
