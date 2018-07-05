# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer
from rest_framework.response import Response


from django.shortcuts import render

# Create your views here.
class UserList(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response (serializer.data)

    def post(self):
        pass

@csrf_exempt
def login_method(request):
    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(username=email, password=password)
    if not user:
        return JsonResponse ({
            "code": 1,
            "error": "error",
        })
    return JsonResponse(UserSerializer(user).data)
@csrf_exempt
def register(request):
    try:
        user = User.objects.create_user(email=request.POST['email'], password=request.POST['password'],
                               username=request.POST['email'], first_name=request.POST['name'],
                               last_name=request.POST['lastname'])

        return JsonResponse(UserSerializer(user).data)
    except:
        return JsonResponse ({
            "code": 1,
            "error": "error",
        })