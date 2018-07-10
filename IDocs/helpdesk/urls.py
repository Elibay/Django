from django.conf.urls import url
from . import views

app_namespace = 'helpdesk'

urlpatterns = [
    url(r'^$', views.UserList.as_view()),
    url(r'^login$', views.login_method, name='login'),
    url(r'^register$', views.register, name='register'),
    url(r'^create_mail$', views.create_mail, name='create_mail'),
    url(r'^get_mails$', views.get_all_mails, name='get_mails'),
    url(r'^get_mails_by_status$', views.get_mails_by_status, name='get_mails_by_status'),
    url(r'^get_mails_by_user$', views.get_mails_by_user, name='get_mails_by_user'),
    url(r'^delete_mail$', views.delete_mail, name='delete_mail'),
]