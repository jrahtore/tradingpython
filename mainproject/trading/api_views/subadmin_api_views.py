from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from users.models import CustomUser

from trading.serializers.custom_api import *

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework import mixins, generics

from rest_framework.decorators import api_view

class GetsubadminAPI(APIView):

    def get(self,request,format=None):
        getuser = CustomUser.objects.filter(user_type='sub_admin')
        serializer = CustomUserSerializer(getuser, many=True)
        return Response(serializer.data)