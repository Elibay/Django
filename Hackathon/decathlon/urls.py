from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('add_cutomers', views.CustomerView)


urlpatterns = [
    url('', include(router.urls)),
    url(r'^authorize/$', views.FunctionView.as_view())
]
