# coding:utf-8
from django.shortcuts import render

# Create your views here.

def home(request):
    info_dict = {'site':'Something of Bottom © Something'}
    return render(request,'home.html',{'tips':'来到 Home','List':[1,2,3,4,5],'info_dict':info_dict})
