from django.conf.urls import url
from . import views

app_namespace = 'helpdesk'

urlpatterns = [
    url(r'^$', views.UserList.as_view()),
    url(r'^login$', views.login_method, name='login'),
    url(r'^register$', views.register, name='register'),
]