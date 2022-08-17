from trading.models import Brokerage_amount
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status

from trading.serializers.brokerage_api import *

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from rest_framework import mixins, generics

from rest_framework.decorators import api_view


class  Brokerage_amountAPI(APIView):

    def get(self, request,pk):
        getuser =  Brokerage_amount.objects.filter(UserWalletID=pk)
      
        serializer =  Brokerage_amountSerializer(getuser, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =  Brokerage_amountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(UserWalletID = CustomUser(id=self.request.data['UserWalletID']),Created_By_id=CustomUser(id=self.request.user.id))
  

            return Response({"Message": "Successfful"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk, format=None):
       
        UserWalletID = pk
        getuser = Brokerage_amount.objects.get(UserWalletID=pk)
        serializer = Brokerage_amountSerializer(getuser, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Brokerage_amount Updated"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    def delete(self, request, pk, format=None):
        id = pk
        getenquiry = Brokerage_amount.objects.get(pk=id)
        getenquiry.delete()
        return Response({"Message": "Brokerage_amount Deleted"})


@api_view(['GET'])
def brokerage_amount(request):
    Detail = Brokerage_amount.objects.filter(UserWalletID = request.user.id)
    serializer = Brokerage_amountSerializer(Detail, many=True)

    return Response(serializer.data)
