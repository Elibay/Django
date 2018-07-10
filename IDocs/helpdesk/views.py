# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import UserSerializer, MailSerializer
from .models import Mail
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

@csrf_exempt
def create_mail(request):
    try:
        Mail.objects.create(status=request.POST['status'], text=request.POST['text'],
                            sender_company=request.POST['sender_company'], priority=request.POST['priority'],
                            sender_email=request.POST['sender_email'], executor=request.POST['executor'],
                            subject=request.POST['subject'])
        return JsonResponse ({
            "code": 0,
            "error": "",
        })
    except:
        return JsonResponse ({
            "code": 1,
            "error": "error",
        })


@csrf_exempt
def get_all_mails(request):
    mails = Mail.objects.all()
    print mails
    serializer = MailSerializer(mails, many=True)
    return Response(serializer.data)

@csrf_exempt
def get_mails_by_user(request):
    mails = Mail.objects.filter(executor=request.POST['executor'])
    serializer = MailSerializer(mails, many=True)
    return Response(serializer.data)

@csrf_exempt
def get_mails_by_status(request):
    mails = Mail.objects.filter(status=request.POST['status'])
    serializer = MailSerializer(mails, many=True)
    return Response(serializer.data)

@csrf_exempt
def delete_mail(request):
    mail = Mail.objects.filter(request['id'])
    mail.is_active = False
