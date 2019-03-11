# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)


def __str__(self):
    return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)


def __str__(self):
    return self.song_title


class Barang (models.Model):
    id = models.AutoField(primary_key=True)
    createdby = models.ForeignKey(
        User, null=True, on_delete=models.CASCADE, default=User, editable=False)
    nama_barang = models.CharField(max_length=100)
    stok = models.IntegerField(default=0)
    waktu = models.DateField(auto_now_add=True)


def __str__(self):
    return self.nama_barang
