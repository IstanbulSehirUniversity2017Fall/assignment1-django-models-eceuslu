# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='main'
urlpatterns = [
    url(r'^period/(?P<period_id>.*)',views.period,name='period'),
    url(r'^author/(?P<author_id>.*)',views.author,name='author'),
    url(r'^book/(?P<book_id>.*)',views.book,name='book'),
    ]