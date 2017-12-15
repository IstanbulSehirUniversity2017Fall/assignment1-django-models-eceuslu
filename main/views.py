from django.shortcuts import render
from .models import AuthorInfo,BookInfo

# Create your views here.

def book(request,index):
    book_index=BookInfo.objects.get(pk=index)
    return render(request,'book.html',{'book':book_index})