from django.shortcuts import render
from .models import Image


def image_gallery(request):
    images = Image.objects.all()
    return render(request, 'event_images/image_gallery.html', {'images': images})
