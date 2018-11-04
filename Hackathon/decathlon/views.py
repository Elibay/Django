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
from django.http import JsonResponse

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

        products = []

        user_id = request.GET.get('user_id')
        user = Customer.objects.get(pk=int(user_id))

        for product in self.queryset:

            ser_product = self.serializer_class(product, many=False).data
            if product in user.favorites.all():
                ser_product['favorite'] = 1
            else:
                ser_product['favorite'] = 0

            products.append(ser_product)

        return Response(products)

    def post(self, request):

        user_id = request.GET.get('user_id')
        product_id = request.GET.get('product_id')
        used_coins = request.GET.get('used_coins')

        user = Customer.objects.get(pk=int(user_id))
        product = Product.objects.get(pk=int(product_id))

        user.products.add(product)
        user.decopoint -= (int(used_coins) - int(product.docoins))
        user.save()

        trns = Transaction.objects.create(product=product, used_coins=used_coins, user=user)
        trns.save()

        return Response({'code': 0, 'user': CustomerSerializer(user, many=False).data})




class ClubView(viewsets.ViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer

    def list(self, request):

        user_id = request.GET.get('user_id', -1)
        user = Customer.objects.get(pk=int(user_id))

        clubs = []

        for club in self.queryset:

            ser_club = self.serializer_class(club, many=False).data
            if club in user.clubs.all():

                ser_club['subscriber'] = True
            else:
                ser_club['subscriber'] = False

            clubs.append(ser_club)


        return Response(clubs)


    def post(self, request):

        try:
            user_id = request.GET.get('user_id', -1)
            club_id = request.GET.get('club_id', -1)
            user = Customer.objects.get(pk=int(user_id))
            club = Club.objects.get(pk=int(club_id))

            user.decopoint += club.decocoins
            user.clubs.add(club)
            user.save()

            clubs = []

            for club in self.queryset:

                ser_club = self.serializer_class(club, many=False).data
                if club in user.clubs.all():

                    ser_club['subscriber'] = True
                else:
                    ser_club['subscriber'] = False

                clubs.append(ser_club)

            return Response({'code': 0, 'new_coins': user.decopoint, 'clubs': clubs})
        except Exception as e:

            return  Response({'code': 1})




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


def authorize(request):

    if request.method == 'GET':
        try:
            email = request.GET.get('email', '')
            password = request.GET.get('password', '')
            user = Customer.objects.get(email=email, password=password)
            print user
            return JsonResponse({'code': 0, 'user': CustomerSerializer(user, many=False).data})
        except Exception as e:
            return JsonResponse({'code': 1})


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

            user_id = request.GET.get('user_id')
            product_id = request.GET.get('product_id')

            product = Product.objects.get(pk=int(user_id))
            user = Customer.objects.get(pk=int(product_id))

            if product in user.favorites.all():
                user.favorites.remove(product)
            else:
                user.favorites.add(product)

            user.save()

            print user.favorites.all()

            return Response({'code': 0})

        except Exception as e:

            return Response({'code': 1})


class SubscribtionClass(viewsets.ViewSet):

    def post(self, request):

        try:
            user_id = request.GET.get('user_id', -1)
            event_id = request.GET.get('event_id', -1)
            user = Customer.objects.get(pk=int(user_id))
            event = Event.objects.get(pk=int(event_id))

            user.decopoint += event.docoins
            user.subscriptions.add(event)
            user.save()

            return Response({'code': 0, 'new_coins': user.decopoint, 'events': EventSerializer(user.subscriptions, many=True).data, 'user': CustomerSerializer(user, many=False).data})
        except Exception as e:

            return  Response({'code': 1})


    def list(self, request):
        try:

            user_id = request.GET.get('user_id', -1)
            user = Customer.objects.get(pk=int(user_id))
            events = Event.objects.filter(customer=user).all()
            return Response({'code': 0, 'events': EventSerializer(events, many=True).data})



        except Exception as e:

            return Response({'code': 1})


    def delete(self, request):

        user_id = request.POST.get('user_id', -1)
        event_id = request.POST.get('event_id', -1)

        user = Customer.objects.get(pk=int(user_id))
        event = Event.objects.get(pk=int(event_id))

        user.subscriptions.remove(event)

        return Response({'code': 0, 'events': EventSerializer(user.subscriptions, many=True).data})



def get_history(request):

    user_id = request.GET.get('user_id', -1)
    user = Customer.objects.get(pk=int(user_id))

    clubs = user.clubs.all()
    products = user.products.all()
    events = user.subscriptions.all()

    history = {'clubs': [], 'products': [], 'events': []}

    for club in clubs:

        ser_club = ClubSerializer(club, many=False).data
        ser_club['subscriber'] = True

        history['clubs'].append(ser_club)

    for product in products:

        ser_prod = ProductSerializer(product, many=False).data
        history['products'].append(ser_prod)

    for event in events:

        ser_event = EventSerializer(event, many=False).data

        history['events'].append(ser_event)

    return JsonResponse(history)




