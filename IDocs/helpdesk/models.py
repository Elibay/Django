# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from rest_framework.response import Response


class Mail(models.Model):
    sender_email = models.CharField(max_length=250)
    sender_company = models.CharField(max_length=250)
    status = models.IntegerField()
    priority = models.IntegerField()
    executor = models.CharField(max_length=250)
    subject = models.CharField(max_length=250)
    text = models.CharField(max_length=1000000)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.subject


