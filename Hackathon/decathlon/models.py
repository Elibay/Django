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
    products = models.ManyToManyField('Product', related_name='products', null=True, blank=True, default=None)
    clubs = models.ManyToManyField('Club', null=True, blank=True)
    favorites = models.ManyToManyField('Product', related_name='favorites', null=True, blank=True)
    photos = models.CharField(max_length=10000, blank=True)
    subscriptions = models.ManyToManyField('Event', default=None, null=True, blank=True)

    def __str__(self):
        return self.email


class Event(models.Model):

    typeOf = models.CharField(max_length=256)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    date = models.CharField(max_length=1000)
    photos = models.CharField(max_length=10000, blank=True)
    docoins = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Club(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    price = models.IntegerField(default=0)
    decocoins = models.IntegerField(default=200)
    photos = models.CharField(max_length=10000)
    subscriber = models.ManyToManyField(Customer, blank=True, null=True)

    def __str__(self):
        return self.title


class Product(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    size = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    photos = models.CharField(max_length=10000)
    type = models.CharField(max_length=100, default='Other')
    docoins = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Transaction(models.Model):

    product = models.ForeignKey(Product)
    user = models.ForeignKey(Customer)
    used_coins = models.IntegerField()


class News(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.title

