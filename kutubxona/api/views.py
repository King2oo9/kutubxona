from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from main.models import BookData
from .serializer import BookSerializer
from rest_framework import permissions
from django.contrib.auth import get_user_model
from rest_framework import viewsets


# Create your views here.


# class BookApiView(ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#     queryset = Bookdata.objects.all()
#     serializer_class = BookSerializer
#
#
# class DetailApiView(RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.AllowAny,)
#     queryset = Bookdata.objects.all()
#     serializer_class = BookSerializer
#
#
# class UserApiView(ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = BookSerializer
#
#
# class DetailUser(RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = BookSerializer

class BookView(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class UserView(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = BookSerializer
