from django.contrib import admin
from playlist.models import Video

# Register your models here.
@admin.register(Video)
class PlaylistAdmin(admin.ModelAdmin):
    pass 
