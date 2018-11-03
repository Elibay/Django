from django.conf.urls import url
from .import views
app_namespace = 'companies'

urlpatterns = [
    url(r'^$', views.StockList.as_view()),
    url(r'^web/(?P<pk>[0-9]+)$', views.ViewStock.as_view()),
    url(r'^xml$', views.get_xml, name='xml')
]