from django.contrib.auth.models import Permission, User
from django.db import models


class Album(models.Model):
    """
        Модель содержит информацию об Альбомах
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    artist = models.CharField(max_length=250)
    title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.artist


class Song(models.Model):
    """
        Модель содержит информацию о Песнях
    """
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title
