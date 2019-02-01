"""djdemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from learn import  views as learn_view
from home import   views as home_view
from article import views as article_view
from zhihudaily import views as zhihudaily_view
from juejin import views as juejin_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',learn_view.index),
    path('calcadd/',learn_view.calcadd,name='calcadd'),
    path('calcadd1/<int:a>/<int:b>/',learn_view.calcadd1,name='calcaadd1'),
    path('home/',home_view.home,name='home'),
    path('article/',article_view.index,name='article'),
    path('newslist/',zhihudaily_view.list,name='newslist'),
    path('zhihusrc/', zhihudaily_view.src, name='zhihusrc'),
    # juejin
    path('juejin/', juejin_view.index, name='juejin'),
    path('juejingetpage/', juejin_view.getPage, name='juejingetpage'),
]
