# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=250)
    password = models.CharField(max_length=250, default='')
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=15)
    age = models.IntegerField(default=0)
    city = models.CharField(max_length=250)
    size = models.CharField(max_length=5)
    decopoint = models.IntegerField(default=0)
    products = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    clubs = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True)
    photos = models.CharField(max_length=10000)
    subscriptions = models.ManyToManyField('Event', default=None, null=True, blank=True)

    def __str__(self):
        return self.email


class Event(models.Model):

    typeOf = models.CharField(max_length=256)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    date = models.CharField(max_length=1000)
    photos = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class Club(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    price = models.IntegerField(default=0)
    photos = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class Product(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    size = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    photos = models.CharField(max_length=10000)
    favorite = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class News(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.title