from django.shortcuts import render, redirect
from .models import Video

# Create your views here.
def playlist(request):
    
    playlist = Video.objects.all()
    return render(request, 'playlist/playlist.html', {'video': playlist})

def add_video(request):
    if request.method == "POST":
        video_title = request.POST['title']
        video_embed = request.POST['embed']
        video_description = request.POST['description']
        Video.objects.create(
            title = video_title,
            embed = video_embed,
            text = video_description
        )
        return redirect('playlist')

    return render(request, 'playlist/add_video.html')