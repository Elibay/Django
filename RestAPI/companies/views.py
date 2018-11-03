# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
from pyexcelerate import Workbook, Color, Style, Font, Fill, Format, Alignment
from django.http import HttpResponse

class StockList(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)
    def post(self, request):
        Stock.objects.create(ticker=request.POST['ticker'], open=request.POST['open'],
                             close=request.POST['close'], volume=request.POST['volume'])
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

class ViewStock(APIView):

    def get(self, request, pk):
        serializer = StockSerializer(Stock.objects.get(id=pk), many=False)
        return Response(serializer.data)
    def post(self):
        pass



def get_xml(request):
    print "1"
    response = HttpResponse(content_type='application/ms-excel')
    print "2"
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    print "3"
    wb = Workbook()
    print "4"
    ws = wb.new_sheet(u'Реестр')
    print "5"
    ws.range("A1", "M1").style.font.bold = True
    print "6"
    fill_xlsx_header(ws)
    print "7"
    wb.save(response)
    return response
def fill_xlsx_header(ws):
    ws.set_cell_value(0, 0, u"#")
    ws.set_cell_value(0, 1, u"Название")
    ws.set_cell_value(0, 2, u"Дата")
    ws.set_cell_value(0, 3, u"Номер")
    ws.set_cell_value(0, 4, u"Сумма")
    ws.set_cell_value(0, 5, u"Направление")
    ws.set_cell_value(0, 6, u"Статус")
    ws.set_cell_value(0, 7, u"Импортирован")
    ws.set_cell_value(0, 8, u"Тип документа")
    ws.set_cell_value(0, 9, u"Контрагент")
    ws.set_cell_value(0, 10, u"Эл. адрес контрагента")
    ws.set_cell_value(0, 11, u'Дата изменения/подписания')
    ws.set_cell_value(0, 12, u'Автор документа')