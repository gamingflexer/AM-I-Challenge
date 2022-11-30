from .views import BaseAPI,video_viewer #,record_status
from . import views
from django.urls import path

urlpatterns = [path('v0/camera/', views.camera_index, name='camera_index'),
               path('v0/camera/<ip>/<int:camera_uid>', views.camera_index, name='camera_index'),
               path('v0/record_status', views.record_status, name='record_status'),
               path('v0/video_viewer/<ip>',video_viewer.as_view() , name='video_viewer'),
               path('v0/testing',BaseAPI.as_view(), name='BaseAPI'),]