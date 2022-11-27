from .views import BaseAPI
from django.urls import path

urlpatterns = [path('api/v0/testing',BaseAPI.as_view(), name='BaseAPI'),]