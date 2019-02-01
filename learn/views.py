# coding: utf-8
from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(u"Hello World")


def calcadd(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(u'calc %s + %s : %s' % (a,b,c))

def calcadd1(request,a,b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

