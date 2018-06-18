from django.shortcuts import render, get_object_or_404
from .models import Album, Song


def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {'albums': albums})


def detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "You didn't select a valid song",
        })
    else:
        song.is_favorite = True
        song.save()
        return render(request, 'music/detail.html', {'album': album})
