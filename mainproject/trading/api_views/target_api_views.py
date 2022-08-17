from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from rest_framework.views import APIView

from trading.serializers.wallet_serializer import *

from trading.models import *


from rest_framework import mixins, generics

from trading.serializers.transaction_serializer import *

from rest_framework.decorators import api_view

import datetime

from datetime import time
from decimal import *

# from trading import Transaction


class TargetAPI(APIView):
    
    def delete(self, format=None):
        Transaction.objects.all().delete()
        return Response({'Message': 'All Recordes Successfully Delete!'}, status.HTTP_200_OK)
        
    def put(self, request, pk, format=None):
        id = pk
        print(request.data, '?????????')
        gettransaction = Transaction.objects.get(pk=id)
        if request.data['Stop_Loss_Value'] is not None:
            print("if")
            print("iff")
            # closeAmount = gettransaction.closeAmount
            # print(closeAmount)
            # gettransaction.Brokerage_amount = int(request.data['Brokerage_amount'])

            gettransaction.Close_amount = int(request.data['Stop_Loss_Value'])

        serializer = TransactionSerializer(gettransaction, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        
            objects = Transaction.objects.get(pk=id)
            print(objects.Close_amount, objects.amount)
            print(request.data['Brokerage_amount'],"objects.Close_amount",objects.Close_amount)
            diff = float(objects.Close_amount) - objects.amount - float(request.data['Brokerage_amount'])
            objects.difference = diff * objects.quantity
            objects.save()
            print(diff,"<<<+================")
            gettransaction.save()
            return Response({"Message": "Transaction Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # serializer = TransactionListingSerializer(getuser, data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response({"Message": "stop loss target Detail Updated", })
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        
class DeleteAPI(APIView):
    
    def delete(self, format=None):
        Transaction.objects.all().delete()
        return Response({'Message': 'All Recordes Successfully Delete!'}, status.HTTP_200_OK)
        
