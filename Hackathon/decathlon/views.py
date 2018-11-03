# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.shortcuts import render

# Create your views here.
class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ClubView(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

class Authorize(APIView):
    def post(self, request):
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        user = Customer.objects.filter(email=email, password=password).first()
        if user:
            serializer = CustomerSerializer(user, many=False)
            return Response({'code': 0, 'user': serializer.data})
        else:
            return Response({'code': 1, 'message': 'error'})

class Register(APIView):
    def post(self, request):
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        name = request.POST.get('name', False)
        phone = request.POST.get('phone', False)
        age = request.POST.get('age', False)
        city = request.POST.get('city', False)
        size = request.POST.get('size', False)
        decopoint = request.POST.get('decopoint', False)
        products = request.POST.get('products', None)
        clubs = request.POST.get('clubs', None)
        photos = request.POST.get('photos', False)
        try:
            user = Product.objects.create(email=email, password=password, name=name,
                                          age=age, phone=phone, city=city, size=size,
                                          decopoint=decopoint, products=products, clubs=clubs, photos=photos)
            serializer = CustomerSerializer(user, many=False)
            return Response({'code': 0, 'user': serializer.data})
        except Exception as e:
            return Response({'code': 1, 'message': e})

class UpdateUser(APIView):
    def post(self, request):
        id = request.POST.get('id', 0)
        bonus = request.POST.get('decopoint', 0)
        user = Customer.objects.get(id=id)
        user.decopoint = bonus
        user.save()

class UpdateProduct(APIView):
    def post(self, request):
        id = request.POST.get('id', 0)
        product = Product.objects.get(id=id)
        product.favorite = request.POST.get('favorite', False)
        product.save()
