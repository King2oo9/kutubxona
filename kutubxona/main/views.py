from django.shortcuts import render, HttpResponse
from .models import BookData


# Create your views here.

def main(request):
    books = BookData.objects.all()
    info = ''
    for i in books:
        info += '<p>' + i.name + ' ' + i.writer + ' ' + i.description + ' ' + i.cost + '</p> <br>'
    return HttpResponse(info)
