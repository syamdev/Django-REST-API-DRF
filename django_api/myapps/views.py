from django.shortcuts import render
from rest_framework import viewsets
from .models import Myapp
from .serializers import MyappSerializer


class MyappView(viewsets.ModelViewSet):
    queryset = Myapp.objects.all()
    serializer_class = MyappSerializer
