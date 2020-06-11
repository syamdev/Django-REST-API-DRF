from rest_framework import serializers
from .models import Myapp


class MyappSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Myapp
        fields = ('id', 'url', 'name', 'language', 'price')
