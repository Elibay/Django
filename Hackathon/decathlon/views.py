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

class FunctionView(APIView):
    def post(self, request):
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)

        user = Customer.objects.filter(email=email, password=password).first()
        print user
        if user:
            serializer = CustomerSerializer(user, many=False)
            return Response({'code': 0, 'user': serializer.data})
        else:
            return Response({'code': 1, 'message': 'error'})
