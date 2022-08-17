from trading.models import Fund
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from trading.serializers.fund_serializers import *

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework import mixins, generics

from rest_framework.decorators import api_view


class FundAPI(APIView):

    def get(self, request,pk):
        getuser = Fund.objects.filter(id=pk)
        # getuser = Fund.objects.all()
        serializer = FundSerializer(getuser, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        
        serializer = FundSerializer(data=request.data)
        if serializer.is_valid():
            Admin = request.user.id
            fund = CustomUser.objects.get(id = Admin)
            serializer.save(UserWalletID = CustomUser(id=self.request.data['UserWalletID']),Created_By_id=CustomUser(id=self.request.user.id))
            return Response({"Message":"Created"},status = status.HTTP_201_CREATED)
        else:
	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        id = pk
        getuser = Fund.objects.get(pk=id)
        serializer = FundSerializer(getuser, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Fund_amount Detail Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id = pk
        getenquiry = Fund.objects.get(pk=id)
        getenquiry.delete()
        return Response({"Message": "Fund_amount Deleted"})
