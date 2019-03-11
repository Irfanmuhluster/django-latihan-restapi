from .models import Album, Song, Barang
from rest_framework import serializers
from django.contrib.auth import get_user_model


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'  # menampilkan semua field pada class Album


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('album', 'song_title')


class BarangSerializer(serializers.ModelSerializer):
    # id = serializers.CharField(max_length=100)
    nama_barang = serializers.CharField(max_length=200)
    stok = serializers.IntegerField()

    # createdby = serializers.CharField(max_length=100)

    # def createdby(self, user):
    #     qs = Barang.objects.filter(whether_like=True, user=user)
    #     serializer = BarangSerializer(instance=qs, many=True)
    #     return serializer.data
    	# createdby = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Barang
        fields = ('__all__')

    # def get_queryset(self, request):
    #     qs = super(BarangSerializer, self).get_queryset(request)
    #     return qs.filter(createdby=request.user)

        # read_only_fields = ('waktu', 'createdby')
