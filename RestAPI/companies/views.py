# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    def post(self):
        print "Hello mtfcs"
        pass

class ViewStock(APIView):

    def get(self, request, pk):
        serializer = StockSerializer(Stock.objects.get(id=pk), many=False)
        return Response(serializer.data)
    def post(self):
        pass