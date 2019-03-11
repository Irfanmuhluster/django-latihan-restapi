# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from api.models import *

# Register your modyyzzzzyyyels here.
# Register your models here.


class BarangAdmin (admin.ModelAdmin):
    list_display = ['id', 'nama_barang', 'stok', 'createdby', 'waktu']
    list_filter = ()
    search_fields = ['id', 'nama_barang']
    list_per_page = 25

    def save_model(self, request, obj, form, change):
        if form.is_valid():
            barang = form.save(commit=False)
            # barang.id = '{0}-{1}' . format(
            #    obj.nama_barang[0:3], request.user.id)
            barang.createdby = request.user
            barang.save()

    def get_queryset(self, request):
        qs = super(BarangAdmin, self).get_queryset(request)
        return qs.filter(createdby=request.user)


admin.site.register(Barang, BarangAdmin)
