# -*- coding: utf-8 -*-

"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf.urls import url, include

from django.views.generic import TemplateView

#import myapp.urls
#import v1.urls

from django.conf import settings
from django.conf.urls.static import static

from django.views import static ##新增,vue/cli4+django 解决static资源请求问题

from django.conf import settings ##新增,vue/cli4+django 解决static资源请求问题



urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^admin/', admin.site.urls),
    #path('polls/', include('polls.urls')),

    #path('accounts/', include('allauth.urls')),
    #path('accounts/', include('myaccount.urls')),
    #path('blog/', include('blog.urls')),
    #path('v1/', include('v1.urls')),
    #path('movies/', include('movies.urls')),
    #path('blogeditor/', include('blogeditor.urls',namespace='blogeditor')),
    #path('xiehuimap/',include('xiehuimap.urls')),
    #path('xiehuimapinfo/',include('xiehuimapinfo.urls')),


    #url(r'^api/', include(myapp.urls)),
    
    url(r'^$', TemplateView.as_view(template_name="wechat.html")),
    #url(r'^$', TemplateView.as_view(template_name="bookapi.html")),
    #url(r'^$/', TemplateView.as_view(template_name="index.html")),
    #url(r'^$', TemplateView.as_view(template_name="echartsmap.html")),

    #url(r'mdeditor/', include('mdeditor.urls')),
    #url(r'ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),
]   
    
#]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#在开发环境里debug模式下，static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 这句是必不可少的，没有的话，你上传的图片将无法显示


#if settings . DEBUG :
#     # static files (images, css, javascript, etc.)
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



