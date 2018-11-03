from django.conf.urls import url, include
from django.contrib import admin
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('add_cutomers', views.CustomerView)
router.register('add_product', views.ProductView)
router.register('clubs', views.ClubView)
router.register('news', views.NewsView)



urlpatterns = [
    url('', include(router.urls)),
    url(r'^authorize/$', views.Authorize.as_view()),
    url(r'^register/$', views.Register.as_view()),
    url(r'^update_user/$', views.UpdateUser.as_view()),
    url(r'^update_product/$', views.UpdateProduct.as_view()),
    url(r'^get_events/$', views.EventView.as_view({'get': 'list'})),
    url(r'^get_products/$', views.ProductView.as_view({'get': 'list'})),
    url(r'^get_clubs/$', views.ClubView.as_view({'get': 'list'})),

]
