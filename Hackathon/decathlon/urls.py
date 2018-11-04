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
    url(r'^authorize/$', views.authorize),
    url(r'^register/$', views.Register.as_view()),
    url(r'^update_user/$', views.UpdateUser.as_view()),
    url(r'^update_product/$', views.UpdateProduct.as_view()),
    url(r'^get_events/$', views.EventView.as_view({'get': 'list'})),
    url(r'^get_products/$', views.ProductView.as_view({'get': 'list'})),
    url(r'^get_clubs/$', views.ClubView.as_view({'get': 'list'})),
    url(r'^get_subscriptions/$', views.SubscribtionClass.as_view({'get': 'list'})),
    url(r'^subscribe_event/$', views.SubscribtionClass.as_view({'post': 'post'})),
    url(r'^unsubscribe_event/$', views.SubscribtionClass.as_view({'delete': 'delete'})),
    url(r'^buy_product/$', views.ProductView.as_view({'post': 'post'})),
    url(r'^subscribe_club/$', views.ClubView.as_view({'post': 'post'})),
    url(r'^get_history/$', views.get_history),




]
