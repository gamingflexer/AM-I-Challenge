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
from firebase_admin import firestore
import json
from api.location import data
db = firestore.client()

video_camera = None
global_frame = None 
# Video Camera API
@csrf_exempt
def camera_index(request,ip,camera_uid):
    i=data[data['camera_uid']==int(camera_uid)]
    camera_info = i.to_dict(orient='records')[0]
    return render(request, 'camera.html',{'ip':ip,'camera_info':camera_info})

@csrf_exempt
def record_status(request):
    data = json.loads(request.body)
    status = data['status']
    ip = data['ip']
    if ip == "":
        ip = 0
    
    global video_camera 
    if video_camera == None:
        video_camera = VideoCamera(ip=ip)

    if status == "true":
        video_camera.start_record()
        return HttpResponse(json.dumps({"status":"true"}))
    else:
        video_camera.stop_record()
        return HttpResponse(json.dumps({"status":"false"}))

def video_stream(ip):
    if ip == "":
        ip = 0
    if ip == "0":
        ip = 0
    if len(str(ip).split(".")) == 4:
        ip = f"rtsp://username:password@{ip}/1"
    
    global video_camera 
    global global_frame

    if video_camera == None:
        video_camera = VideoCamera(ip=ip)
        
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
    def get(self, request,ip):
        return StreamingHttpResponse(video_stream(ip), content_type='multipart/x-mixed-replace; boundary=frame')

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
        

def dashboard_data_main(only_firebase=False):
    if only_firebase:
        docs = db.collection(u'alerts').stream()
        data = {}
        for doc in docs:
            data.update({doc.id : doc.to_dict()})
        context = []
        for i in data:
            context.append({'lat':data[i]['lat'], 
                            'lng':data[i]['long'],
                            'uid':data[i]['uid'],
                            'time':str(data[i]['time'])})
        return context
    else:
        data = {}
        alerts_ref = db.collection(u'alerts')
        docs = alerts_ref.stream()
        for doc in docs:
            data.update({doc.id : doc.to_dict()})
        context = []
        for i in data:
            context.append({'lat':data[i]['lat'], 
                            'lng':data[i]['long'],
                            'uid':data[i]['uid'],
                            'time':str(data[i]['time']),
                            'location':""})
        return context
    