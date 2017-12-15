# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
    url(r'^book/(?P<index>.*)$', views.book, name='book'),
    url(r'^author/(?P<index>.*)$', views.author, name='author')
    ]