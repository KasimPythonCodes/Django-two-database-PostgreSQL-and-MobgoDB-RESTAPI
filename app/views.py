from django.shortcuts import render
from app.serializers import UserRegistrationSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response 
from rest_framework import status
from app.models import Registration
from rest_framework import serializers
from django.contrib.auth.hashers import make_password
# Create your views here.

class UserRegistration(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = Registration.objects.all()
    
    def post(self ,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_pic =serializer.validated_data['user_pic']
        fullname =serializer.validated_data['fullname']
        phone_no =serializer.validated_data['phone_no']
        email =serializer.validated_data['email']
        password =serializer.validated_data['password']
        # print(make_password(password), ";;;;;;;;;;;;;;;;;;;;;;;;;;;;")
        if Registration.objects.filter(email=email).exists():
            raise serializers.ValidationError("Email already exists")
        else:    
            Obj= Registration(fullname=fullname ,phone_no=phone_no ,email=email ,password=make_password(password))
            Obj.save()
            Obj_Image= Registration(user_pic=user_pic)
            Obj_Image.save(using='mongo_db')
            # print(serializer.validated_data['user_pic'] , "KKKKKKKKKKKKKKKKKKkk")
            return Response(serializer.data)


class UserRegistrationViews(GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = Registration.objects.all()
    queryset = Registration.objects.all().using('mongo_db')
    def get(self , request ,pk=None):
        try:
            user_id = Registration.objects.get(pk = pk)
            img_id = Registration.objects.all().using('mongo_db').get(id=user_id.id)
            user_id.user_pic = img_id.user_pic
            if user_id ==None and  img_id == None and user_id==img_id :
                return Response(f"User Id {user_id}  not Found")
            serializer = self.serializer_class(user_id)
            return Response(serializer.data) 
        except Exception as e:
            raise serializers.ValidationError({"Error":f"User with Id: {pk} not found"})
        
        
        
