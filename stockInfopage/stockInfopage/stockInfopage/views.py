

from django.shortcuts import render

from .models import Question
from .models import Book
from .models import Daily

def book(request):
    info = Book.objects.all()
    context = {'info':info}
    return render(request, 'stockInfopage/test.html', context)

def daily_price(request):
    info = Daily.objects.all()
    context = {'info':info}
    return render(request, 'stockInfopage/daily_price.html',context)
