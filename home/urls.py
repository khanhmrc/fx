from django.urls import path
from django.contrib import admin
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('chart',views.chart,name='chart'),
    #path('chart1',views.chart1,name='chart1'),
    path('test',views.test,name='test'),
    path('live',views.live,name='live'),
    path('contact',views.contact,name='contact'),
    path('404',views.err404,name='404'),
]