# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import action

from django.shortcuts import render

import json
# Create your views here.


class CustomerView(viewsets.ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class NewsView(viewsets.ModelViewSet):

    queryset = News.objects.all()
    serializer_class = NewsSerializer

class ProductView(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):

        products = self.serializer_class(self.queryset, many=True)
        return Response(products.data)


class ClubView(viewsets.ViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def list(self, request):

        clubs = self.serializer_class(self.queryset, many=True)
        return Response(clubs.data)


class EventView(viewsets.ViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def list(self, request):

        events = self.serializer_class(self.queryset, many=True)
        return Response(events.data)

# class EventView(APIView):
#
#
#     def get(self, request):
#
#         events = Event.objects.all()
#         serializer = EventSerializer(events)
#
#         return Response({'code': 0, 'events': serializer.data})


class Authorize(APIView):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        user = Customer.objects.filter(email=email, password=password).first()
        if user:
            serializer = CustomerSerializer(user, many=False)
            return Response({'code': 0, 'user': serializer.data})
        else:
            return Response({'code': 1, 'message': 'error'})

class Register(APIView):
    def post(self, request):
        data = json.loads(request.body)
        email = data['email']
        password = data['password']
        name = data['name']
        phone = data['phone']
        age = data['age']
        city = data['city']
        size = data['size']
        decopoint = data['decopoint']
        products = data['products']
        clubs = data['clubs']
        photos = data['photos']
        try:
            user = Customer.objects.create(email=email, password=password, name=name,
                                          age=age, phone=phone, city=city, size=size,
                                          decopoint=decopoint, products=products, clubs=clubs, photos=photos)
            serializer = CustomerSerializer(user, many=False)
            return Response({'code': 0, 'user': serializer.data})
        except Exception as e:
            return Response({'code': 1, 'message': e})

class UpdateUser(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            id = data['id']
            bonus = data['decopoint']
            user = Customer.objects.get(id=id)
            user.decopoint = bonus
            user.save()
            return Response({'code': 0})
        except Exception as e:
            return Response({'code': 1, 'message': e})

class UpdateProduct(APIView):


    def post(self, request):


        try:
            data = json.loads(request.body)

            id = int(data['id'])
            favorite = int(data['favorite'])

            product = Product.objects.get(id=id)
            product.favorite = favorite
            product.save()
            return Response({'code': 0})

        except Exception as e:

            return Response({'code': 1})


def SubscribtionClass():
    print "hello"