# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

admin.site.register(Customer)
admin.site.register(Event)
admin.site.register(Club)
admin.site.register(Product)
admin.site.register(Transaction)


# Register your models here.
