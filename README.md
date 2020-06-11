# Django-REST-API-DRF
Build REST API with Django Rest Framework

### Install Django

- `pip install django`
- `pip install djangorestframework`

### Start Project
- `django-admin.py startproject django_api`
- in settings.py:
    ```
    INSTALLED_APPS = [
        [...]
        'rest_framework',
    ]
    ```
- `python manage.py migrate`
- `python manage.py runserver`

### Create App
- `python manage.py startapp myapps`
- in settings.py:
    ```
    INSTALLED_APPS = [
        [...]
        'rest_framework',
        'myapps',
    ]
    ```
- in django_api/urls.py:
    ```
    from django.contrib import admin
    from django.urls import path, include
    
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myapps.urls')),
    ]
    ```
- in myapps/urls.py:
    ```
    from django.urls import path, include
    from . import views
    
    
    urlpatterns = [
    
    ]
    ```

### Admin Area
- `python manage.py createsuperuser`
- create login data

### Create Model Class
- in myapps/models.py:
    ```
    from django.db import models
    
    
    class Myapp(models.Model):
        name = models.CharField(max_length=200)
        language = models.CharField(max_length=100)
        price = models.CharField(max_length=10)
    ```
- `python manage.py makemigrations`
- `python manage.py migrate`

### Add Model to Admin Area
- in myapps/admin.py:
    ```
    from django.contrib import admin
    from .models import Myapp
    
    
    admin.site.register(Myapp)
    ```
- Add data in admin page
- in myapps/models.py:
    ```
    [...]  
    class Myapp(models.Model):
        name = models.CharField(max_length=200)
        language = models.CharField(max_length=100)
        price = models.CharField(max_length=10)

        def __str__(self):
            return self.name    
    ```

### Create Serializer
- create file myapps/serializers.py
- in myapps/serializers.py:
    ```
    from rest_framework import serializers
    from .models import Myapp
    
    
    class MyappSerializer(serializers.ModelSerializer):
        class Meta:
            model = Myapp
            fields = ('id', 'name', 'language', 'price')
    ```

### Create Views
- in myapps/views.py:
    ```
    from django.shortcuts import render
    from rest_framework import viewsets
    from .models import Myapp
    from .serializers import MyappSerializer
    
    
    class MyappView(viewsets.ModelViewSet):
        queryset = Myapp.objects.all()
        serializer_class = MyappSerializer
    ```

### Create URLs & Routes
- in myapps/urls.py:
    ```
    from django.urls import path, include
    from . import views
    from rest_framework import routers
    
    router = routers.DefaultRouter()
    router.register('myapps', views.MyappView)
    
    
    urlpatterns = [
        path('', include(router.urls)),
    ]
    ```
- `python manage.py runserver`
- Check django page. API page is running.

### Switch to Hyperlinked Serializers
- Test add data from page form
- in myapps/serializers.py:
    ```
    class MyappSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Myapp
            fields = ('id', 'url', 'name', 'language', 'price')
    ```
- Check API page again.

### Install Postman
- Check http://127.0.0.1:8000/myapps on Postman 
