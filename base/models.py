from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tag(models.Model):
    name = models.TextField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)   
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/', null=True)
    description = models.TextField(null=True, blank=True)
    # participant = 
    
    def __str__(self) -> str:
        return self.name

class Playlist(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    link = models.TextField()

    def __str__(self) -> str:
        return self.link
    

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.body[0:50]