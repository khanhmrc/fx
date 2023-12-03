from http.client import HTTPResponse
from django.shortcuts import render
import requests 
from forex_python.converter import CurrencyRates
from alpha_vantage.foreignexchange import ForeignExchange
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import json
from django.http import JsonResponse
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from collections import namedtuple 
from alpha_vantage.foreignexchange import ForeignExchange
import oandapyV20
from oandapyV20.exceptions import V20Error
from oandapyV20.endpoints.instruments import InstrumentsCandles

def home(request):
    # Đường dẫn tới file Excel
    excel_file = 'data/data.xlsx'

    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(excel_file)

    # Lấy dữ liệu từ cột 'No' và 'amount'
    trades = df['trades'].tolist()
    amounts = df['amount'].tolist()

    # Tạo context chứa dữ liệu để truyền cho template
    context = {
        'trades': trades,
        'amounts': amounts,
    }

    return render(request, 'home/index2.html', context)
def test(request):
    context={
    }
    return render(request,'home/test.html',context)
def contact(request):
    context={
    }
    return render(request,'home/contact.html',context)

#api_key= 'T88L4BBZY8O1586X'
def chart(request):
    
    # Đường dẫn tới file Excel
    excel_file = 'data/data.xlsx'

    # Đọc dữ liệu từ file Excel
    df = pd.read_excel(excel_file)

    # Lấy dữ liệu từ cột 'No' và 'amount'
    trades = df['trades'].tolist()
    amounts = df['amount'].tolist()

    # Tạo context chứa dữ liệu để truyền cho template
    context = {
        'trades': trades,
        'amounts': amounts,
    }

    return render(request, 'home/chart.html', context)

def live(request):
    context={
    }
    return render(request,'home/live.html',context)

def err404(request):
    context={
    }
    return render(request,'home/404.html',context)