# coding: utf-8
from django.shortcuts import render
from django.http import  HttpResponse
import json
import string
import urllib
import ssl
# Create your views here.

headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "utf-8",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "content-type": "application/json;charset=UTF-8",
}

def list(request):
    try:
     _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
      # Legacy Python that doesn't verify HTTPS certificates by default
      pass
    else:
      # Handle target environment that doesn't support HTTPS verification
     ssl._create_default_https_context = _create_unverified_https_context
    url = 'https://news-at.zhihu.com/api/4/news/latest'
    req = urllib.request.Request(url, headers=headers)
    s = urllib.request.urlopen(req).read().decode('utf-8')
    return render(request, 'list.html',{'info_dict':s})

def src(request):
    id = request.GET.get('id')
    try:
     _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
      # Legacy Python that doesn't verify HTTPS certificates by default
      pass
    else:
      # Handle target environment that doesn't support HTTPS verification
     ssl._create_default_https_context = _create_unverified_https_context
    url = 'https://news-at.zhihu.com/api/4/news/' + id
    print(id)
    req = urllib.request.Request(url, headers=headers)
    s = urllib.request.urlopen(req).read().decode('utf-8')
    return render(request, 'zhihusrc.html', {'info_dict': s})
    # return HttpResponse(s)

def getArticle(request):
    try:
     _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
      # Legacy Python that doesn't verify HTTPS certificates by default
      pass
    else:
      # Handle target environment that doesn't support HTTPS verification
     ssl._create_default_https_context = _create_unverified_https_context
    url = 'https://interface.meiriyiwen.com/article/random?dev=1'
    req = urllib.request.Request(url, headers=headers)
    s = urllib.request.urlopen(req).read().decode('utf-8')
    ss = json.loads(s)
    print(ss)
    return HttpResponse(ss)
