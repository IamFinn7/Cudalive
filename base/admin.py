from django.contrib import admin
from .models import Room, Message, Playlist, Tag
# Register your models here.

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Playlist)
admin.site.register(Tag)