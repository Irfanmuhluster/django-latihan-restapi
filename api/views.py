from .models import Album, Song, Barang
# from django.shortcuts import get_object_or_404
# from rest_framework import generics, permissions
from django.http import Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AlbumSerializer, SongSerializer, BarangSerializer


class BarangViewSet(viewsets.ModelViewSet):
    queryset = Barang.objects.all()
    serializer_class = BarangSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Barang.objects.filter(createdby=user)

    # def get(self, request, format=None):
    #     serializer = BarangSerializer(request.user)
    #     return Response(serializer.data)
    #     if request.user.is_authenticated():
    #         queryset = Barang.objects.all()
    #         serializer_class = BarangSerializer

    #         def get_queryset(self):
    #             """
    #             This view should return a list of all the purchases
    #             for the currently authenticated user.
    #             """
    #             user = self.request.user
    #             return Barang.objects.filter(createdby=user)
    #     else:
    #         Barangs = Barang.objects.all()
    #         serializer = BarangSerializer(Barangs, many=True)
    #         return Response(serializer.data)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class DeleteBarang(APIView):

    def get(self, request, format=None):
        Barangs = Barang.objects.all()
        serializer = BarangSerializer(Barangs, many=True)
        return Response(serializer.data)

    # def get_queryset(self, request, format=None):
    #     qs = super(BarangSerializer, self).get_queryset(request)
    #     return qs.filter(createdby=request.user)

    def delete(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# kalau pake viewsets.ModelViewSet harus pakai query set
# kalau pake query set terus filter lalu logout maka error tidak boleh anonimou
# pakai auten
class BarangList(APIView):
    """
    List all Barangs, or create a new Barang.
    """

    def get(self, request, format=None):
        Barangs = Barang.objects.all()
        serializer = BarangSerializer(Barangs, many=True)
        return Response(serializer.data)

    def post(self, request, obj, form, change, format=None):
        # ini merequest data dari serialized
        serializer = BarangSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BarangDetail(APIView):
    """
    Retrieve, update or delete a Barang instance.
    """

    def get_object(self, pk):
        try:
            return Barang.objects.get(pk=pk)
        except Barang.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang = BarangSerializer(Barang)
        return Response(Barang.data)

    def put(self, request, pk, format=None):
        Barang = self.get_object(pk)
        serializer = BarangSerializer(Barang, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Barang = self.get_object(pk)
        Barang.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class UpdateBarang(generics.RetrieveUpdateDestroyAPIView):
#     # def get_queryset(self):
#     queryset = Barang.objects.all()
#     serializer_class = BarangSerializer

#     pass


# class DeleteBarang(generics.DestroyAPIView):
#     # def get_queryset(self):
#     queryset = Barang.objects.all()
#     serializer_class = BarangSerializer

#     # def get_queryset(self):
#     # 	return
#     pass


# class Barang(generics.ListCreateAPIView):
#     queryset = Barang.objects.all()
#     permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = BarangSerializer

    # def perform_create(self, serializers):
    # 	serializers.save()
