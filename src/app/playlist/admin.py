from django.contrib import admin
from .models import Playlist, PlaylistItem

class PlaylistItemInline(admin.TabularInline):
    model = PlaylistItem
    extrat = 0


class PlaylistAdmin(admin.ModelAdmin):
    inlines = [PlaylistItemInline]

    class Meta:
        model = Playlist

admin.site.register(Playlist, PlaylistAdmin)
# Register your models here.
