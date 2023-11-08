from rest_framework import serializers
from app.models import Registration

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id','user_pic','fullname','phone_no','email' ,'password']
        