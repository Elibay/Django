from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('helpdesk.urls', namespace='helpdesk')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
