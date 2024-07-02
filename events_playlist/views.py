# playlists/views.py
from django.shortcuts import render
from .models import Song


def playlist(request):
    songs = Song.objects.all()
    return render(request, 'events_playlist/playlist.html', {'songs': songs})
