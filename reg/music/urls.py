from django.conf.urls import url
from . import views

app_namespace = 'music'

urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^registration/$', views.UserFormView.as_view(), name='registration'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    url(r'album/(?P<pk>[0-9]+)/edit/$', views.AlbumEdit.as_view(), name='album-edit'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]