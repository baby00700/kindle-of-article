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
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
}

def index(request):
    #ssl._create_default_https_context = ssl._create_unverified_context
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
    return render(request, 'article.html',{'tips':'来到 Home','List':[1,2,3,4,5],'info_dict':ss})
