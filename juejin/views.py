# coding: utf-8
from django.shortcuts import render
from django.http import  HttpResponse
import json
import string
import urllib
import ssl
from bs4 import BeautifulSoup
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
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    data = {
        "category": "frontend",
        "order": "heat",
        "offset": 0,
        "limit": 30,
    }
    url = 'https://extension-ms.juejin.im/resources/gold'
    postdata = json.dumps(data).encode('utf-8')
    req = urllib.request.Request(url, data=postdata, headers=headers)
    s = urllib.request.urlopen(req).read().decode('utf-8')
    ss = json.loads(s)
    return render(request, 'juejinlist.html', {'info_dict': ss})

def getPage(request):
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    url = request.GET.get('url')
    req = urllib.request.Request(url, headers=headers)
    s = urllib.request.urlopen(req).read().decode('utf-8')
    soup = BeautifulSoup(s)
    htmlTitle = soup.title.contents
    html = soup.article.find_all(class_="article-content")
    return render(request, 'juejinpage.html', {'info_dict': html[0],'title':htmlTitle[0]})