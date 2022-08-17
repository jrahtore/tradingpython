from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from users.models import CustomUser

from trading.serializers.custom_api import *

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework import mixins, generics

from rest_framework.decorators import api_view

from rest_framework.authentication import BasicAuthentication

from rest_framework.permissions import IsAuthenticated

class CustomUserAPI(APIView):
    def patch(self, request, pk, format=None):
        serializer = CustomUserSerializer(data=request.data)
        id = pk
        getuser = CustomUser.objects.get(pk=id)
      
        serializer = CustomUserSerializer(getuser, data=request.data)


        if serializer.is_valid():
            password = serializer.validated_data.get('password')
            serializer.validated_data['password']=make_password(password)
            serializer.save()
        
            return Response({"Message": "User Detail Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,format=None):
        getuser = CustomUser.objects.filter(created_by= self.request.user.id)
        serializer = CustomUserSerializer(instance=getuser, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = CustomUserSerializer(data=request.data)
        getuser = CustomUser.objects.get(id=self.request.user.id)
        serializer = CustomUserSerializer(getuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Watch list Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


