from django.contrib import admin
from .models import Album, Photo


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at')
    search_fields = ('title', 'user__username')
    list_filter = ('created_at',)


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('caption', 'album', 'uploaded_at')
    search_fields = ('caption',)
    list_filter = ('uploaded_at',)