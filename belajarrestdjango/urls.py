"""belajarrestdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
# router.register(r'album', views.AlbumViewSet)
# router.register(r'song', views.SongViewSet)
# router.register(r'barang', BarangViewSet)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/produk/', BarangList.as_view()),
    url(r'^api/barang/delete', DeleteBarang.as_view()),
    url(r'^api/barang/(?P<pk>[0-9]+)/$', BarangDetail.as_view()),
    # url(r'^api/barang/(?P<pk>[0-9]+)/delete', DeleteBarang.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/barang/(?P<pk>\d+)/delete$', BarangDestroyView.as_view()),
    # url(r'^api/barang/(?P<pk>\d+)/update$', BarangUpdateView.as_view()),
]
