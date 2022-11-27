from rest_framework import serializers
from api.models import *
        
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta():
        model = UserInfo
        fields = "__all__"
