from django.shortcuts import render,redirect
from .models import AuthorInfo,BookInfo,PeriodInfo
from .forms import PeriodInfoForm,AuthorInfoForm,BookInfoForm
# Create your views here.


def period(request,period_id):
    if period_id:
        period=PeriodInfo.objects.get(pk=period_id)
        authors=AuthorInfo.objects.filter(literary_period=period)
        return render(request,'period.html',{'authors':authors,'period':period})
    else:
        if request.method=='POST':
            form = PeriodInfoForm(data=request.POST,instance=PeriodInfo.objects.get(pk=request.POST['id']))
            if form.is_valid():form.save()
            return redirect('http://127.0.0.1:8000/main/period/'+request.POST['id'])
        else:
            periods=[]
            for period in PeriodInfo.objects.all():periods.append((period,PeriodInfoForm(instance=period)))
            return render(request, 'period.html', {'periods':periods})

def author(request,author_id):
    if author_id:
        author=AuthorInfo.objects.get(pk=author_id)
        books=BookInfo.objects.filter(author=author)
        return render(request,'author.html',{'books':books,'author':author})
    else:
        if request.method=='POST':
            form = AuthorInfoForm(data=request.POST,instance=AuthorInfo.objects.get(pk=request.POST['id']))
            if form.is_valid():form.save()
            return redirect('http://127.0.0.1:8000/main/author/'+request.POST['id'])
        else:
            authors=[]
            for author in AuthorInfo.objects.all():authors.append((author,AuthorInfoForm(instance=author)))
            return render(request, 'author.html', {'authors':authors})

def book(request,book_id):
    if book_id:
        book=BookInfo.objects.get(pk=book_id)
        return render(request,'book.html',{'book':book})
    else:
        if request.method=='POST':
            form = BookInfoForm(data=request.POST,instance=BookInfo.objects.get(pk=request.POST['id']))
            if form.is_valid():form.save()
            return redirect('http://127.0.0.1:8000/main/book/'+request.POST['id'])
        else:
            books=[]
            for book in BookInfo.objects.all():books.append((book,BookInfoForm(instance=book)))
            return render(request, 'book.html', {'books':books})