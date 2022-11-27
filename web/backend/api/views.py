from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from .serializers import UserInfoSerializer
from .models import UserInfo
from api.config import basepath
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
