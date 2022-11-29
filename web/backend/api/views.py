from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializers import UserInfoSerializer
from flask import jsonify
from .models import UserInfo
from api.config import basepath
from api.camera import VideoCamera
from django.http import StreamingHttpResponse,HttpResponse
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
import json

video_camera = None
global_frame = None 
            
# Video Camera API
@csrf_exempt
def camera_index(request):
    return render(request, 'camera.html')

@csrf_exempt
def record_status(request):
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera()

    data = json.loads(request.body)

    status = data['status']

    if status == "true":
        video_camera.start_record()
        return HttpResponse(json.dumps({"status":"true"}))
    else:
        video_camera.stop_record()
        return HttpResponse(json.dumps({"status":"false"}))

def video_stream():
    global video_camera 
    global global_frame

    if video_camera == None:
        video_camera = VideoCamera()
        
    while True:
        frame = video_camera.get_frame()

        if frame != None:
            global_frame = frame
            yield (b'--frame\r\n'
                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            yield (b'--frame\r\n'
                            b'Content-Type: image/jpeg\r\n\r\n' + global_frame + b'\r\n\r\n')
            
class video_viewer(APIView):
    @csrf_exempt
    def get(self, request):
        return StreamingHttpResponse(video_stream(), content_type='multipart/x-mixed-replace; boundary=frame')

# Create your views here.
class BaseAPI(APIView):

    def get(self, request):
        try:
            result = ""
            context = {
                'data': result
            }
            return Response(context, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_200_OK)
        
    

def dashboard_data_main(user):
    users_list = UserInfo.objects.filter(user=user)
    users_list_serializer_data = UserInfoSerializer(users_list, many=True).data
    context = []
    for user_single in users_list_serializer_data:
        if user_single['user'] == user:
            context.append({"user":user,"total_uploads":user_single['total_uploads'],"in_progress":user_single['in_progress']})
            return context[0]
        else:
            data_map = {"user":user}
            serialized = UserInfoSerializer(data=data_map)
            if serialized.is_valid():
                serialized.save()
