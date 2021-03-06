# coding: utf-8
from django.shortcuts import render
from django.http import  HttpResponse
import json
import string
import urllib
import ssl
from article.models import Article
from django.core import serializers
from django.db.models import Count, Sum
# Create your views here.


def typeof(variate):
  type = None
  if isinstance(variate, int):
          type = "int"
  elif isinstance(variate, str):
          type = "str"
  elif isinstance(variate, float):
          type = "float"
  elif isinstance(variate, list):
          type = "list"
  elif isinstance(variate, tuple):
          type = "tuple"
  elif isinstance(variate, dict):
          type = "dict"
  elif isinstance(variate, set):
          type = "set"
  return type


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
      pass
    else:
      ssl._create_default_https_context = _create_unverified_https_context
    url = 'https://interface.meiriyiwen.com/article/random?dev=1'
    req = urllib.request.Request(url, headers=headers)
    s = urllib.request.urlopen(req).read().decode('utf-8')
    ss = json.loads(s)
    print(ss)
    return render(request, 'article.html',{'tips':'来到 Home','List':[1,2,3,4,5],'info_dict':ss})


def getArticle(request):
    try:
      _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
      pass
    else:
      ssl._create_default_https_context = _create_unverified_https_context
    url = 'https://interface.meiriyiwen.com/article/random?dev=1'
    req = urllib.request.Request(url, headers=headers)
    s = urllib.request.urlopen(req).read().decode('utf-8')
    Article.objects.create(con=s)
    pageindex = int(request.GET['pageindex'])
    pagesize = int(request.GET['pagesize'])
    outPut = Article.objects.all().order_by('-id')[pagesize*(pageindex - 1):pagesize*(pageindex-1)+pagesize]
    nums = Article.objects.all().aggregate(Count("id"))
    print(typeof(nums))
    print(typeof(serializers.serialize("json", outPut)))
    # print(serializers.serialize("json", nums))
    return HttpResponse(json.dumps({'count': str(json.dumps(nums['id__count'])), 'data': serializers.serialize("json", outPut)}), content_type='application/json')


def getArticleDetial(request):
  id = request.GET['id']
  outPut = Article.objects.get(id=id)
  return HttpResponse(outPut, content_type='application/json')

