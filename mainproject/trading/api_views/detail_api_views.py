from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from users.models import CustomUser

from trading.serializers.wallet_serializer import *

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework import mixins, generics

from rest_framework.decorators import api_view


class detailAPI(APIView):

    def get(self,request,format=None):
        getuser = UserWallet.objects.all()
        serializer = detailWalletSerializer(getuser, many=True)
        return Response(serializer.data)