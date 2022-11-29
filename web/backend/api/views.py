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
from home.utils import location_finder
import json

db = firestore.client()

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
                            'time':str(data[i]['time'])[:10]})
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
                            'time':str(data[i]['time'])[:10],
                            'location':location_finder(data[i]['lat'],data[i]['long'])})
        return context
    
# dashboard_data_main()
# def add_data():
#     test = {'lat': 52.9920608091255, 'uid': '5JfRGbdmdvfdp2X7M517IFGIKtOi1', 'long': 0.22862492630344, 'time': firestore.SERVER_TIMESTAMP}
#     db.collection("alerts").add(test)
    
# add_data()